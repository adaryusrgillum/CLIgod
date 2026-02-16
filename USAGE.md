# CLIgod Usage Guide

Complete guide to using CLIgod for multi-agent content creation.

## Quick Start

```bash
# 1. Initialize configuration
python3 -m cligod.cli init

# 2. Edit .env with your API keys
nano .env

# 3. Verify configuration
python3 -m cligod.cli check-config

# 4. Create your first content
python3 -m cligod.cli create "AI trends in 2024"
```

## Commands

### `init` - Initialize Configuration

Creates a `.env` file from the template.

```bash
python3 -m cligod.cli init
```

Output:
```
🚀 Initializing CLIgod
✅ Created .env file from template
📝 Next steps:
  1. Edit .env and add your API keys
  2. Run 'cligod check-config' to verify configuration
  3. Run 'cligod create "your topic"' to create content
```

### `check-config` - Verify Configuration

Checks that all API keys and settings are properly configured.

```bash
python3 -m cligod.cli check-config
```

Output:
```
🔍 Configuration Status

API Keys:
  Gemini API Key: ✅ Set
  Claude API Key: ✅ Set
  Kimi API Key: ✅ Set

Vertex AI Configuration:
  Project ID: ✅ Set
  Location: us-east5
  Access Token: ✅ Set
...
```

### `create` - Generate Content

Create content using the 6-stage pipeline.

**Basic Usage:**
```bash
python3 -m cligod.cli create "Your Topic Here"
```

**With Citation Style:**
```bash
python3 -m cligod.cli create "Climate Change" --citation-style MLA
```

**For Specific Platform:**
```bash
python3 -m cligod.cli create "Marketing Tips" --platform linkedin
```

**Save Output:**
```bash
python3 -m cligod.cli create "AI Ethics" --output results.json
```

**Verbose Mode (Show All Stages):**
```bash
python3 -m cligod.cli create "Technology Trends" --verbose
```

**Complete Example:**
```bash
python3 -m cligod.cli create "The Future of Remote Work" \
  --citation-style APA \
  --platform linkedin \
  --output remote-work.json \
  --verbose
```

## Command Options

### create

| Option | Short | Type | Description |
|--------|-------|------|-------------|
| `--citation-style` | `-c` | Choice | Citation style: APA or MLA (default: APA) |
| `--platform` | `-p` | Choice | Target platform: twitter, linkedin, facebook, instagram |
| `--output` | `-o` | Path | Save output to file |
| `--verbose` | `-v` | Flag | Show all pipeline stages |
| `--config` | | Path | Custom config.yaml path |

## Understanding the Pipeline

### Stage 1: RESEARCH (Gemini with Grounding)
**Agent:** Gemini with Google Search  
**Purpose:** Conduct deep research on the topic

The agent:
- Searches current information using Google Search
- Identifies trends and developments
- Finds credible sources
- Extracts key insights and statistics
- Identifies SEO keywords

**Output:** Comprehensive research document with sources

### Stage 2: WRITE (Gemini)
**Agent:** Gemini Writer  
**Purpose:** Create first draft

The agent:
- Writes engaging content based on research
- Applies proper citation format (APA/MLA)
- Optimizes for SEO
- Structures for target platform
- Includes hooks and CTAs

**Output:** Complete first draft with citations

### Stage 3: REVIEW (Claude)
**Agent:** Claude Reviewer  
**Purpose:** Critical analysis and feedback

The agent checks:
- Clarity and readability
- Accuracy and facts
- Citation quality
- SEO optimization
- Engagement potential
- Grammar and style

**Output:** Detailed editorial feedback

### Stage 4: REWRITE (Gemini)
**Agent:** Gemini Rewriter  
**Purpose:** Incorporate feedback

The agent:
- Addresses all valid criticisms
- Improves clarity and engagement
- Fixes errors
- Maintains core message
- Enhances SEO

**Output:** Revised draft

### Stage 5: POLISH (Kimi)
**Agent:** Kimi Polisher  
**Purpose:** Optimize flow and readability

The agent:
- Smooths transitions
- Enhances conversational tone
- Varies sentence structure
- Improves pacing
- Maintains accuracy

**Output:** Polished content

### Stage 6: FINAL CHECK (Claude)
**Agent:** Claude Checker  
**Purpose:** Quality gate

The agent evaluates:
- Overall quality
- Accuracy
- Citations
- SEO
- Platform readiness

**Output:** PASS/FAIL decision with justification

## Output Files

When using `--output`, CLIgod creates two files:

### 1. JSON File (Full Pipeline Data)

**Example:** `output.json`

```json
{
  "topic": "AI trends in 2024",
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

### 2. Markdown File (Content Only)

**Example:** `output.md`

Contains only the final polished content, ready to use.

## Examples

### Example 1: Basic Tech Article

```bash
python3 -m cligod.cli create "Quantum Computing in 2024"
```

### Example 2: Academic Content with MLA

```bash
python3 -m cligod.cli create "Impact of Social Media on Mental Health" \
  --citation-style MLA \
  --output mental-health.json
```

### Example 3: LinkedIn Professional Post

```bash
python3 -m cligod.cli create "Leadership Skills for Tech Managers" \
  --platform linkedin \
  --citation-style APA
```

### Example 4: Twitter Thread

```bash
python3 -m cligod.cli create "5 AI Tools Every Developer Should Know" \
  --platform twitter \
  --output ai-tools.json
```

### Example 5: Full Pipeline with Verbose Output

```bash
python3 -m cligod.cli create "Sustainable Technology Solutions" \
  --citation-style APA \
  --platform linkedin \
  --output sustainability.json \
  --verbose
```

This shows all 6 stages in detail.

## Advanced Usage

### Custom Configuration File

Use a custom `config.yaml`:

```bash
python3 -m cligod.cli create "Topic" --config /path/to/config.yaml
```

### Environment Variables

Override `.env` settings:

```bash
GEMINI_API_KEY=xxx CLAUDE_API_KEY=yyy python3 -m cligod.cli create "Topic"
```

### Batch Processing

Create a script to process multiple topics:

```bash
#!/bin/bash
topics=(
  "AI Ethics"
  "Quantum Computing"
  "Green Technology"
)

for topic in "${topics[@]}"; do
  python3 -m cligod.cli create "$topic" \
    --output "output/${topic// /-}.json"
done
```

### Platform-Specific Optimization

Different platforms have different requirements:

**Twitter:**
- Short, punchy content
- More hashtags (3-5)
- Emoji usage
- Thread format

**LinkedIn:**
- Professional tone
- Longer form (500-1000 words)
- Industry insights
- Clear takeaways

**Facebook:**
- Conversational tone
- Visual descriptions
- Engagement questions
- Community focus

**Instagram:**
- Visual storytelling
- Shorter paragraphs
- Emoji-friendly
- Hashtag strategy

## Tips for Best Results

### 1. Be Specific with Topics

❌ "Technology"  
✅ "How AI is Transforming Healthcare Diagnostics in 2024"

### 2. Choose the Right Platform

Match your topic to platform strengths:
- LinkedIn: Professional, B2B, career topics
- Twitter: News, quick insights, tech updates
- Facebook: Community, lifestyle, how-to content
- Instagram: Visual topics, behind-the-scenes

### 3. Use Verbose Mode for Learning

```bash
--verbose
```

See how each agent transforms the content.

### 4. Review Failed Quality Gates

If Stage 6 returns FAIL:
- Read the feedback carefully
- Adjust your topic or approach
- Try again with more specific guidance

### 5. Experiment with Citation Styles

- **APA**: Sciences, social sciences, technical topics
- **MLA**: Humanities, literature, arts

### 6. Save Everything

Always use `--output` to:
- Keep a record of all stages
- Learn from the process
- Reuse research
- Build a content library

## Common Workflows

### 1. Research-First Workflow

```bash
# Step 1: Research only (Stage 1)
python3 -m cligod.cli create "Topic" --verbose > research.txt

# Review research, then continue
python3 -m cligod.cli create "Refined Topic" --output final.json
```

### 2. Multi-Platform Campaign

```bash
# LinkedIn version
python3 -m cligod.cli create "Topic" --platform linkedin -o linkedin.json

# Twitter version
python3 -m cligod.cli create "Topic" --platform twitter -o twitter.json

# Facebook version
python3 -m cligod.cli create "Topic" --platform facebook -o facebook.json
```

### 3. Iterative Improvement

```bash
# First attempt
python3 -m cligod.cli create "Topic" -o v1.json

# Review output, refine topic
python3 -m cligod.cli create "Refined Topic" -o v2.json

# Final version
python3 -m cligod.cli create "Final Topic" -o final.json --verbose
```

## Troubleshooting

### Content Not Meeting Quality Gate

**Problem:** Stage 6 returns FAIL

**Solutions:**
1. Make topic more specific
2. Review Stage 3 feedback
3. Try different platform
4. Adjust citation style

### API Rate Limits

**Problem:** "Rate limit exceeded"

**Solutions:**
1. Wait and retry
2. Check API quotas
3. Upgrade API plan if needed

### Poor Quality Content

**Problem:** Content doesn't meet expectations

**Solutions:**
1. Use more specific topics
2. Review verbose output to see where it went wrong
3. Adjust agent personas in config.yaml
4. Provide more context in the topic

### Pipeline Timeout

**Problem:** Pipeline takes too long

**Solutions:**
1. Check internet connection
2. Verify API key validity
3. Try simpler topic first
4. Check API service status

## Best Practices

1. **Start Simple**: Begin with basic topics to understand the flow
2. **Use Verbose Mode**: Learn how each stage works
3. **Save Everything**: Always use `--output` for records
4. **Review Stages**: Check Stage 3 and 6 feedback
5. **Iterate**: Refine topics based on results
6. **Backup API Keys**: Store securely, separate from code
7. **Monitor Usage**: Track API costs and usage
8. **Version Content**: Save different versions of outputs

## Integration with Workflows

### With Git

```bash
# Create content
python3 -m cligod.cli create "Topic" -o content.json

# Review and commit
git add content.json content.md
git commit -m "Add AI trends article"
```

### With CI/CD

```yaml
# .github/workflows/content.yml
name: Generate Content
on:
  workflow_dispatch:
    inputs:
      topic:
        description: 'Topic to generate content for'
        required: true

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate content
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          CLAUDE_API_KEY: ${{ secrets.CLAUDE_API_KEY }}
          KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}
        run: |
          python3 -m cligod.cli create "${{ github.event.inputs.topic }}" \
            --output content.json
```

### With CMS

Export to your CMS:

```python
import json

# Load generated content
with open('content.json') as f:
    data = json.load(f)

# Extract final content
content = data['final_content']

# Post to your CMS
# ... your CMS integration code
```

## Support

For help:
1. Check this guide
2. Run `python3 -m cligod.cli --help`
3. Review [README.md](README.md)
4. Check [examples/](examples/)
5. Open an issue on GitHub

---

**Happy Content Creating!** 🚀
