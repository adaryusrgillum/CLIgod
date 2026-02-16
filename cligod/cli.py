"""CLI interface for CLIgod."""

import click
import logging
import json
import sys
from pathlib import Path
from datetime import datetime

from .config import Config
from .pipeline import ContentPipeline


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version='0.1.0')
def cli():
    """CLIgod - Multi-agent content creation pipeline
    
    Create trendy APA/MLA formatted, SEO-enriched social media content
    using a 6-stage multi-agent pipeline with Gemini, Claude, and Kimi.
    """
    pass


@cli.command()
@click.argument('topic')
@click.option('--citation-style', '-c', type=click.Choice(['APA', 'MLA']), 
              default='APA', help='Citation style to use')
@click.option('--platform', '-p', type=click.Choice(['twitter', 'linkedin', 'facebook', 'instagram']),
              help='Target social media platform')
@click.option('--output', '-o', type=click.Path(), help='Output file path')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output showing all stages')
@click.option('--config', type=click.Path(exists=True), help='Path to config.yaml')
def create(topic, citation_style, platform, output, verbose, config):
    """Create content on a given TOPIC using the 6-stage pipeline.
    
    Example:
        cligod create "AI trends in 2024" --citation-style APA --platform linkedin
    """
    try:
        # Load configuration
        cfg = Config(config_path=config) if config else Config()
        
        # Validate API keys
        if not cfg.gemini_api_key:
            click.echo("Error: GEMINI_API_KEY not set in environment", err=True)
            sys.exit(1)
        if not cfg.claude_api_key:
            click.echo("Error: CLAUDE_API_KEY not set in environment", err=True)
            sys.exit(1)
        if not cfg.kimi_api_key:
            click.echo("Error: KIMI_API_KEY not set in environment", err=True)
            sys.exit(1)
        
        # Initialize and run pipeline
        click.echo(f"\n🚀 Starting CLIgod content creation pipeline")
        click.echo(f"📝 Topic: {topic}")
        click.echo(f"📚 Citation Style: {citation_style}")
        if platform:
            click.echo(f"📱 Platform: {platform}")
        click.echo()
        
        pipeline = ContentPipeline(cfg)
        result = pipeline.run(topic, citation_style, platform)
        
        # Display results
        if verbose:
            click.echo("\n" + "="*80)
            click.echo("STAGE 1: RESEARCH (Gemini with grounding)")
            click.echo("="*80)
            click.echo(result['stages']['research'])
            
            click.echo("\n" + "="*80)
            click.echo("STAGE 2: WRITE (Gemini)")
            click.echo("="*80)
            click.echo(result['stages']['draft'])
            
            click.echo("\n" + "="*80)
            click.echo("STAGE 3: REVIEW (Claude)")
            click.echo("="*80)
            click.echo(result['stages']['review'])
            
            click.echo("\n" + "="*80)
            click.echo("STAGE 4: REWRITE (Gemini)")
            click.echo("="*80)
            click.echo(result['stages']['revision'])
            
            click.echo("\n" + "="*80)
            click.echo("STAGE 5: POLISH (Kimi)")
            click.echo("="*80)
            click.echo(result['stages']['polish'])
            
            click.echo("\n" + "="*80)
            click.echo("STAGE 6: FINAL CHECK (Claude)")
            click.echo("="*80)
            click.echo(result['stages']['final_check'])
        
        # Display final content
        click.echo("\n" + "="*80)
        click.echo("✨ FINAL CONTENT")
        click.echo("="*80)
        click.echo(result['final_content'])
        
        # Display quality gate result
        click.echo("\n" + "="*80)
        if result['passed_quality_gate']:
            click.echo("✅ QUALITY GATE: PASS")
        else:
            click.echo("❌ QUALITY GATE: FAIL")
        click.echo("="*80)
        
        # Save to file if requested
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save as JSON with all stages
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            # Also save just the final content as markdown
            content_path = output_path.with_suffix('.md')
            with open(content_path, 'w', encoding='utf-8') as f:
                f.write(result['final_content'])
            
            click.echo(f"\n💾 Results saved to:")
            click.echo(f"   - Full output: {output_path}")
            click.echo(f"   - Content only: {content_path}")
        
        click.echo("\n✅ Pipeline completed successfully!")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}", exc_info=True)
        click.echo(f"\n❌ Error: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
def check_config():
    """Check configuration and API key status."""
    try:
        cfg = Config()
        
        click.echo("\n🔍 Configuration Status\n")
        
        # Check API keys
        click.echo("API Keys:")
        click.echo(f"  Gemini API Key: {'✅ Set' if cfg.gemini_api_key else '❌ Not set'}")
        click.echo(f"  Claude API Key: {'✅ Set' if cfg.claude_api_key else '❌ Not set'}")
        click.echo(f"  Kimi API Key: {'✅ Set' if cfg.kimi_api_key else '❌ Not set'}")
        
        # Check Vertex AI config
        click.echo("\nVertex AI Configuration:")
        click.echo(f"  Project ID: {'✅ Set' if cfg.vertex_project_id else '❌ Not set'}")
        click.echo(f"  Location: {cfg.vertex_location if cfg.vertex_location else '❌ Not set'}")
        click.echo(f"  Access Token: {'✅ Set' if cfg.vertex_access_token else '❌ Not set'}")
        
        # Check proxy config
        click.echo("\nProxy Configuration:")
        click.echo(f"  HTTP Proxy: {cfg.http_proxy if cfg.http_proxy else 'Not set'}")
        click.echo(f"  HTTPS Proxy: {cfg.https_proxy if cfg.https_proxy else 'Not set'}")
        
        # Check settings
        click.echo("\nContent Settings:")
        click.echo(f"  Default Citation Style: {cfg.default_citation_style}")
        click.echo(f"  Default Output Format: {cfg.default_output_format}")
        
        click.echo()
        
    except Exception as e:
        click.echo(f"\n❌ Error checking configuration: {str(e)}", err=True)
        sys.exit(1)


@cli.command()
def init():
    """Initialize CLIgod configuration."""
    click.echo("\n🚀 Initializing CLIgod\n")
    
    # Check if .env exists
    env_path = Path('.env')
    if env_path.exists():
        overwrite = click.confirm('.env file already exists. Overwrite?')
        if not overwrite:
            click.echo("Initialization cancelled.")
            return
    
    # Create .env from template
    template_path = Path(__file__).parent.parent / '.env.example'
    if template_path.exists():
        import shutil
        shutil.copy(template_path, env_path)
        click.echo("✅ Created .env file from template")
    else:
        # Create basic .env
        with open(env_path, 'w') as f:
            f.write("# CLIgod Configuration\n")
            f.write("GEMINI_API_KEY=your-gemini-api-key\n")
            f.write("CLAUDE_API_KEY=your-claude-api-key\n")
            f.write("KIMI_API_KEY=your-kimi-api-key\n")
        click.echo("✅ Created basic .env file")
    
    click.echo("\n📝 Next steps:")
    click.echo("  1. Edit .env and add your API keys")
    click.echo("  2. Run 'cligod check-config' to verify configuration")
    click.echo("  3. Run 'cligod create \"your topic\"' to create content")
    click.echo()


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()
