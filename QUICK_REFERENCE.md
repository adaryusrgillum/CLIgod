# CLIgod Quick Reference

## Installation

```bash
git clone https://github.com/adaryusrgillum/CLIgod.git
cd CLIgod
pip install -r requirements.txt
python3 -m cligod.cli init
# Edit .env with your API keys
python3 -m cligod.cli check-config
```

## Commands

### Create Content
```bash
# Basic
python3 -m cligod.cli create "Your Topic"

# Full options
python3 -m cligod.cli create "Topic" \
  --citation-style [APA|MLA] \
  --platform [twitter|linkedin|facebook|instagram] \
  --output filename.json \
  --verbose
```

### Check Configuration
```bash
python3 -m cligod.cli check-config
```

### Initialize
```bash
python3 -m cligod.cli init
```

## API Keys Required

1. **Gemini**: https://makersuite.google.com/app/apikey
2. **Claude**: https://console.anthropic.com/
3. **Kimi**: https://platform.moonshot.cn/

## Pipeline Stages

1. 🔍 **RESEARCH** (Gemini + Google Search) - Find current info
2. ✍️ **WRITE** (Gemini) - Create first draft
3. 🔎 **REVIEW** (Claude) - Critical analysis
4. ♻️ **REWRITE** (Gemini) - Apply feedback
5. ✨ **POLISH** (Kimi) - Optimize readability
6. ✅ **FINAL CHECK** (Claude) - Quality gate

## Examples

```bash
# Tech article
python3 -m cligod.cli create "AI in Healthcare 2024"

# Academic with MLA
python3 -m cligod.cli create "Climate Change Effects" \
  --citation-style MLA --output climate.json

# LinkedIn post
python3 -m cligod.cli create "Leadership Tips" \
  --platform linkedin --verbose

# Save and see all stages
python3 -m cligod.cli create "Tech Trends" \
  --output trends.json --verbose
```

## Configuration Files

### .env
```bash
GEMINI_API_KEY=your-key
CLAUDE_API_KEY=your-key
KIMI_API_KEY=your-key
VERTEX_PROJECT_ID=your-project
VERTEX_LOCATION=us-east5
```

### config.yaml
```yaml
agents:
  gemini_research:
    model: "gemini-pro"
    temperature: 0.7
    persona: "..."
```

## Output

- **JSON file**: Complete pipeline data (all 6 stages)
- **Markdown file**: Final content only
- **Console**: Progress and final result

## Cost Estimate

~$0.04-0.18 per complete pipeline run

## Project Stats

- **Lines of Code**: ~1,150
- **Python Files**: 9
- **Agents**: 3 (Gemini, Claude, Kimi)
- **Stages**: 6
- **Documentation**: 6 files

## File Structure

```
CLIgod/
├── cligod/              # Main package
│   ├── agents/         # Agent implementations
│   ├── cli.py          # CLI interface
│   ├── config.py       # Configuration
│   └── pipeline.py     # Orchestrator
├── examples/           # Usage examples
├── config.yaml         # Agent config
├── .env.example        # Template
└── requirements.txt    # Dependencies
```

## Documentation

- **README.md** - Overview
- **INSTALL.md** - Installation guide
- **USAGE.md** - Detailed usage
- **ARCHITECTURE.md** - Technical details
- **PROJECT_SUMMARY.md** - Complete summary
- **QUICK_REFERENCE.md** - This file

## Troubleshooting

### Import Error
```bash
pip install -r requirements.txt
```

### API Key Not Set
```bash
# Check .env exists in current directory
cat .env
# Or set directly
export GEMINI_API_KEY=xxx
```

### Test Installation
```bash
python3 test_installation.py
```

## Key Features

✅ Multi-agent collaboration (agents review each other)  
✅ APA/MLA citation formatting  
✅ SEO optimization  
✅ Social media ready  
✅ Google Search grounding  
✅ Platform-specific content  
✅ Quality gate (PASS/FAIL)  
✅ Enterprise proxy support  

## Version

**v0.1.0** - Beta Release

## Links

- Repository: https://github.com/adaryusrgillum/CLIgod
- Issues: https://github.com/adaryusrgillum/CLIgod/issues

## License

MIT License

---

**Quick Start:**
```bash
git clone https://github.com/adaryusrgillum/CLIgod.git
cd CLIgod
pip install -r requirements.txt
python3 -m cligod.cli init
# Edit .env
python3 -m cligod.cli create "Your Topic"
```

🚀 **Happy Content Creating!**
