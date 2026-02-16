# CLIgod 🚀

Multi-agent content creation pipeline for developing trendy APA/MLA formatted, SEO-enriched social media content using AI agents that correct and improve each other's work.

## Overview

CLIgod implements a sophisticated 6-stage content creation pipeline:

1. **RESEARCH** (Gemini w/ grounding) → Deep topic research with real-time web search
2. **WRITE** (Gemini) → First draft using research findings
3. **REVIEW** (Claude) → Critical review + corrections
4. **REWRITE** (Gemini) → Incorporate Claude's feedback
5. **POLISH** (Kimi) → Final flow/readability pass
6. **FINAL CHECK** (Claude) → Quality gate, pass/fail decision

## Features

✨ **Multi-Agent Architecture**: Agents with different personas critique and improve each other's work  
📚 **Citation Support**: Automatic APA and MLA citation formatting  
🔍 **SEO Optimization**: Built-in SEO enrichment and keyword optimization  
📱 **Social Media Ready**: Optimized for Twitter, LinkedIn, Facebook, Instagram  
🌐 **Real-Time Research**: Gemini with Google Search grounding for current information  
🔧 **Configurable**: Flexible configuration via YAML and environment variables  
🏢 **Enterprise Ready**: Support for corporate proxies and Vertex AI

## Installation

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - Google Gemini API or Vertex AI
  - Anthropic Claude API
  - Moonshot AI (Kimi) API

### Install from source

```bash
git clone https://github.com/adaryusrgillum/CLIgod.git
cd CLIgod
pip install -e .
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Initialize configuration

```bash
cligod init
```

This creates a `.env` file from the template.

### 2. Add your API keys

Edit `.env` and add your API keys:

```bash
# Gemini API Configuration
GEMINI_API_KEY=your-gemini-api-key-here

# Claude API Configuration
CLAUDE_API_KEY=your-claude-api-key-here

# Kimi API Configuration
KIMI_API_KEY=your-kimi-api-key-here

# Vertex AI Configuration (optional, for Gemini with grounding)
VERTEX_PROJECT_ID=your-project-id
VERTEX_LOCATION=us-east5
VERTEX_ACCESS_TOKEN=your-vertex-access-token
```

### 3. Verify configuration

```bash
cligod check-config
```

## Usage

### Basic Content Creation

```bash
cligod create "AI trends in 2024"
```

### With Options

```bash
# Specify citation style
cligod create "Machine Learning in Healthcare" --citation-style MLA

# Target specific platform
cligod create "Social Media Marketing Tips" --platform linkedin

# Save output to file
cligod create "Climate Change Solutions" --output results.json

# Verbose mode (show all stages)
cligod create "Blockchain Technology" --verbose
```

### Full Example

```bash
cligod create "The Future of Remote Work" \
  --citation-style APA \
  --platform linkedin \
  --output remote-work-content.json \
  --verbose
```

This will:
1. Research the topic using Gemini with Google Search grounding
2. Write a first draft optimized for LinkedIn
3. Have Claude review and critique the draft
4. Rewrite based on Claude's feedback
5. Polish the content with Kimi for optimal flow
6. Final quality check by Claude
7. Save all stages and final content to `remote-work-content.json` and `remote-work-content.md`

## Pipeline Stages

### Stage 1: Research (Gemini with Grounding)
- Conducts deep research using Google Search
- Identifies trends and recent developments
- Finds credible sources
- Extracts key insights and statistics
- Identifies SEO keywords and hashtags

### Stage 2: Write (Gemini)
- Creates engaging first draft
- Incorporates research findings
- Applies proper citation format
- Optimizes for SEO
- Structures for social media

### Stage 3: Review (Claude)
- Critical analysis of draft
- Checks accuracy and clarity
- Reviews citations
- Evaluates SEO optimization
- Assesses engagement potential
- Provides actionable feedback

### Stage 4: Rewrite (Gemini)
- Incorporates Claude's feedback
- Addresses all criticisms
- Maintains core message
- Enhances quality and engagement

### Stage 5: Polish (Kimi)
- Optimizes flow and readability
- Improves transitions
- Enhances conversational tone
- Refines pacing
- Preserves facts and citations

### Stage 6: Final Check (Claude)
- Quality gate evaluation
- Pass/fail decision
- Final validation of:
  - Accuracy
  - Clarity
  - Citations
  - SEO
  - Social media readiness

## Configuration Files

### config.yaml

Customize agent behavior, personas, and settings:

```yaml
agents:
  gemini_research:
    model: "gemini-pro"
    temperature: 0.7
    max_tokens: 8000
    use_grounding: true
    persona: "You are an expert researcher..."
  
  # ... other agents
```

### .env

Store API keys and credentials securely:

```bash
GEMINI_API_KEY=your-key
CLAUDE_API_KEY=your-key
KIMI_API_KEY=your-key
```

## Corporate Proxy Setup

For enterprise environments with corporate proxies:

```bash
# Enable Vertex AI
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Configure corporate proxy
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=https://your-proxy:port
```

## Advanced Features

### Custom Agent Personas

Edit `config.yaml` to customize how each agent behaves:

```yaml
agents:
  claude_reviewer:
    persona: |
      You are a meticulous editor specializing in technical content.
      Focus on accuracy, clarity, and technical depth.
```

### SEO Configuration

Adjust SEO parameters:

```yaml
seo:
  keyword_density_target: 0.02
  meta_description_length: 160
  title_length_max: 60
```

### Social Media Optimization

Configure platform-specific settings:

```yaml
social_media:
  platforms:
    - twitter
    - linkedin
  optimization:
    hashtag_count_max: 5
    emoji_usage: moderate
```

## Output Format

The tool generates two files:

1. **JSON file** (e.g., `output.json`): Complete pipeline data including all stages
2. **Markdown file** (e.g., `output.md`): Final polished content only

### JSON Structure

```json
{
  "topic": "Your Topic",
  "citation_style": "APA",
  "target_platform": "linkedin",
  "timestamp": "2024-02-16T10:00:00",
  "stages": {
    "research": "...",
    "draft": "...",
    "review": "...",
    "revision": "...",
    "polish": "...",
    "final_check": "..."
  },
  "final_content": "...",
  "passed_quality_gate": true
}
```

## Troubleshooting

### API Key Issues

```bash
# Check configuration
cligod check-config

# Ensure .env file is in current directory or set environment variables
export GEMINI_API_KEY=your-key
```

### Vertex AI Setup

For Gemini with grounding, ensure Vertex AI is properly configured:

```bash
# Authenticate with Google Cloud
gcloud auth application-default login

# Set project
gcloud config set project your-project-id
```

### Import Errors

```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## CLI Reference

### Commands

- `cligod create TOPIC` - Create content on a topic
- `cligod check-config` - Check configuration status
- `cligod init` - Initialize configuration files

### Options for `create`

- `-c, --citation-style [APA|MLA]` - Citation style (default: APA)
- `-p, --platform [twitter|linkedin|facebook|instagram]` - Target platform
- `-o, --output PATH` - Save output to file
- `-v, --verbose` - Show all pipeline stages
- `--config PATH` - Custom config.yaml path

## Integration with Other CLI Agents

CLIgod can work alongside other CLI development tools:

- **Claude Code**: Deep reasoning and architecture analysis
- **Aider**: Git-native workflows and multi-file coordination
- **OpenCode**: Provider-agnostic LLM support
- **Codex CLI**: Rapid prototyping
- **Gemini CLI**: Multimodal capabilities
- **Warp**: Terminal replacement with agentic features
- **Plandex**: Multi-file tasks with sandbox mode

## Architecture

```
CLIgod/
├── cligod/
│   ├── __init__.py
│   ├── cli.py           # CLI interface
│   ├── config.py        # Configuration management
│   ├── pipeline.py      # Pipeline orchestration
│   └── agents/
│       ├── __init__.py
│       ├── base.py      # Base agent class
│       ├── gemini_agent.py
│       ├── claude_agent.py
│       └── kimi_agent.py
├── config.yaml          # Agent configurations
├── .env.example         # Environment template
├── requirements.txt     # Dependencies
├── setup.py            # Package setup
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review configuration examples

## Roadmap

- [ ] Add support for more LLM providers
- [ ] Web interface for pipeline visualization
- [ ] Batch processing multiple topics
- [ ] Custom agent training
- [ ] Integration with content management systems
- [ ] A/B testing for different agent configurations
- [ ] Analytics and performance metrics
- [ ] Multi-language support

---

Made with ❤️ by the CLIgod Team