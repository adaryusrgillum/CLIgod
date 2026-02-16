"""Configuration management for CLIgod."""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv


class Config:
    """Manages configuration for CLIgod."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize configuration.
        
        Args:
            config_path: Path to config.yaml file. If None, looks in current directory.
        """
        # Load environment variables
        load_dotenv()
        
        # Load YAML config
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config.yaml"
        
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        # API Keys
        self.gemini_api_key = os.getenv('GEMINI_API_KEY')
        self.claude_api_key = os.getenv('CLAUDE_API_KEY')
        self.kimi_api_key = os.getenv('KIMI_API_KEY')
        
        # Vertex AI Configuration
        self.vertex_project_id = os.getenv('VERTEX_PROJECT_ID')
        self.vertex_location = os.getenv('VERTEX_LOCATION', 'us-east5')
        self.vertex_access_token = os.getenv('VERTEX_ACCESS_TOKEN')
        
        # Proxy Configuration
        self.http_proxy = os.getenv('HTTP_PROXY')
        self.https_proxy = os.getenv('HTTPS_PROXY')
        
        # Content Settings
        self.default_citation_style = os.getenv('DEFAULT_CITATION_STYLE', 'APA')
        self.default_output_format = os.getenv('DEFAULT_OUTPUT_FORMAT', 'markdown')
    
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """Get configuration for a specific agent.
        
        Args:
            agent_name: Name of the agent (e.g., 'gemini_research')
        
        Returns:
            Dictionary with agent configuration
        """
        return self.config.get('agents', {}).get(agent_name, {})
    
    def get_citation_style(self, style: str) -> Dict[str, Any]:
        """Get citation style configuration.
        
        Args:
            style: Citation style (APA or MLA)
        
        Returns:
            Dictionary with citation style rules
        """
        return self.config.get('citation_styles', {}).get(style, {})
    
    def get_seo_config(self) -> Dict[str, Any]:
        """Get SEO configuration."""
        return self.config.get('seo', {})
    
    def get_social_media_config(self) -> Dict[str, Any]:
        """Get social media configuration."""
        return self.config.get('social_media', {})
