# CLIgod Architecture

## System Overview

CLIgod is a multi-agent content creation system that uses three different LLM providers (Gemini, Claude, and Kimi) in a 6-stage pipeline where agents review and improve each other's work.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CLIgod System                                │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────┐
│   User Input    │
│   (Topic)       │
└────────┬────────┘
         │
         v
┌─────────────────────────────────────────────────────────────────────┐
│                    CLI Interface (cli.py)                            │
│  - Command parsing (Click)                                           │
│  - Input validation                                                  │
│  - Output formatting                                                 │
└────────┬────────────────────────────────────────────────────────────┘
         │
         v
┌─────────────────────────────────────────────────────────────────────┐
│              Configuration Manager (config.py)                       │
│  - Load .env file                                                    │
│  - Load config.yaml                                                  │
│  - Manage API keys                                                   │
│  - Validate settings                                                 │
└────────┬────────────────────────────────────────────────────────────┘
         │
         v
┌─────────────────────────────────────────────────────────────────────┐
│           Pipeline Orchestrator (pipeline.py)                        │
│  - Initialize all agents                                             │
│  - Coordinate 6-stage workflow                                       │
│  - Pass context between stages                                       │
│  - Collect results                                                   │
└────────┬────────────────────────────────────────────────────────────┘
         │
         ├──────────────────────────────────────────────────────┐
         │                                                       │
         v                                                       v
┌─────────────────┐                                    ┌─────────────────┐
│   STAGE 1       │                                    │   STAGE 2       │
│   RESEARCH      │────────────────────────────────>│   WRITE         │
│                 │                                    │                 │
│  Gemini Agent   │  Research Data                    │  Gemini Agent   │
│  (w/ Grounding) │  + Sources                        │  (Writer)       │
└─────────────────┘                                    └────────┬────────┘
                                                                 │
                                                                 v
                                                        ┌─────────────────┐
                                                        │   STAGE 3       │
                                                        │   REVIEW        │
                                                        │                 │
                                                        │  Claude Agent   │
                                                        │  (Reviewer)     │
                                                        └────────┬────────┘
                                                                 │
                                                                 v
                                                        ┌─────────────────┐
                                                        │   STAGE 4       │
                                                        │   REWRITE       │
                                                        │                 │
                                                        │  Gemini Agent   │
                                                        │  (Rewriter)     │
                                                        └────────┬────────┘
                                                                 │
                                                                 v
                                                        ┌─────────────────┐
                                                        │   STAGE 5       │
                                                        │   POLISH        │
                                                        │                 │
                                                        │  Kimi Agent     │
                                                        │  (Polisher)     │
                                                        └────────┬────────┘
                                                                 │
                                                                 v
                                                        ┌─────────────────┐
                                                        │   STAGE 6       │
                                                        │   FINAL CHECK   │
                                                        │                 │
                                                        │  Claude Agent   │
                                                        │  (Checker)      │
                                                        └────────┬────────┘
                                                                 │
                                                                 v
                                                        ┌─────────────────┐
                                                        │  Final Output   │
                                                        │  - JSON         │
                                                        │  - Markdown     │
                                                        │  - PASS/FAIL    │
                                                        └─────────────────┘
```

## Component Details

### 1. CLI Interface (`cligod/cli.py`)

**Responsibilities:**
- Parse command-line arguments
- Validate user input
- Initialize configuration
- Execute commands (create, check-config, init)
- Format and display output
- Save results to files

**Commands:**
- `create` - Run the 6-stage pipeline
- `check-config` - Verify configuration
- `init` - Initialize .env file

### 2. Configuration Manager (`cligod/config.py`)

**Responsibilities:**
- Load environment variables from .env
- Load agent configurations from config.yaml
- Validate API keys
- Provide configuration to other components

**Configuration Sources:**
- `.env` - API keys and credentials
- `config.yaml` - Agent settings and personas

### 3. Pipeline Orchestrator (`cligod/pipeline.py`)

**Responsibilities:**
- Initialize all 6 agents
- Execute stages in sequence
- Pass context between stages
- Aggregate results
- Determine pass/fail status

**Stages:**
1. Research (Gemini w/ grounding)
2. Write (Gemini)
3. Review (Claude)
4. Rewrite (Gemini)
5. Polish (Kimi)
6. Final Check (Claude)

### 4. Agent System (`cligod/agents/`)

#### Base Agent (`base.py`)
**Abstract base class for all agents**
- Defines common interface
- Manages persona and configuration
- Provides prompt building utilities

#### Gemini Agent (`gemini_agent.py`)
**Google's Gemini/PaLM models**
- Supports standard Gemini API
- Supports Vertex AI with grounding
- Used in Stages 1, 2, and 4
- Handles both API and Vertex AI modes

#### Claude Agent (`claude_agent.py`)
**Anthropic's Claude models**
- Uses Anthropic API
- Used in Stages 3 and 6
- Specialized for critical analysis

#### Kimi Agent (`kimi_agent.py`)
**Moonshot AI's Kimi models**
- REST API integration
- Used in Stage 5
- Specialized for readability

## Data Flow

### Input Flow
```
User Topic
  ↓
CLI Parser
  ↓
Configuration Loader
  ↓
Pipeline Orchestrator
  ↓
Agent Initialization
```

### Pipeline Flow
```
Topic → Research → Draft → Review → Revision → Polish → Check → Final Output
        (Stage 1) (Stage 2) (Stage 3) (Stage 4) (Stage 5) (Stage 6)
```

### Output Flow
```
Final Content
  ↓
JSON File (all stages)
  ↓
Markdown File (content only)
  ↓
Console Display
```

## Agent Communication

### Stage 1 → Stage 2
```
Research Output:
- Key findings
- Sources
- Statistics
- Keywords
  ↓
Draft Input
```

### Stage 2 → Stage 3
```
Draft Output:
- Complete article
- Citations
- SEO elements
  ↓
Review Input
```

### Stage 3 → Stage 4
```
Review Output:
- Critical feedback
- Issues identified
- Suggestions
  ↓
Rewrite Input
```

### Stage 4 → Stage 5
```
Revision Output:
- Improved draft
- Corrections applied
  ↓
Polish Input
```

### Stage 5 → Stage 6
```
Polished Output:
- Final content
- Optimized flow
  ↓
Check Input
```

### Stage 6 → Output
```
Check Result:
- PASS/FAIL decision
- Quality assessment
  ↓
Final Output
```

## Configuration Files

### `.env`
```
GEMINI_API_KEY=xxx
CLAUDE_API_KEY=xxx
KIMI_API_KEY=xxx
VERTEX_PROJECT_ID=xxx
VERTEX_LOCATION=xxx
```

### `config.yaml`
```yaml
agents:
  gemini_research:
    model: "gemini-pro"
    temperature: 0.7
    persona: "..."
  # ... other agents
```

## External Dependencies

### LLM Providers
1. **Google Gemini**
   - API: `google-generativeai`
   - Vertex AI: `google-cloud-aiplatform`
   
2. **Anthropic Claude**
   - API: `anthropic`
   
3. **Moonshot Kimi**
   - REST API: `requests`

### Supporting Libraries
- `click` - CLI framework
- `python-dotenv` - Environment variables
- `pyyaml` - YAML parsing
- `requests` - HTTP requests

## Security Considerations

### API Key Management
- Stored in `.env` file (gitignored)
- Never committed to version control
- Loaded securely via python-dotenv

### Proxy Support
- HTTP/HTTPS proxy configuration
- Corporate proxy compatibility
- Environment-based configuration

### Error Handling
- API key validation
- Network error handling
- Rate limit management
- Graceful degradation

## Scalability

### Parallel Processing (Future)
Currently sequential, but designed for:
- Parallel research from multiple sources
- Concurrent agent initialization
- Batch processing multiple topics

### Caching (Future)
Potential for:
- Research result caching
- Agent response caching
- Configuration caching

### Monitoring (Future)
Could add:
- Performance metrics
- API usage tracking
- Quality metrics
- Cost tracking

## Extension Points

### Custom Agents
Add new agents by:
1. Extending `BaseAgent`
2. Implementing `generate()` method
3. Adding to `config.yaml`
4. Integrating into pipeline

### New Stages
Add stages by:
1. Creating new agent
2. Adding method to `ContentPipeline`
3. Updating pipeline flow
4. Documenting new stage

### Custom Workflows
Create workflows by:
1. Subclassing `ContentPipeline`
2. Overriding stage methods
3. Adding custom logic
4. Maintaining interface

## Testing Strategy

### Unit Tests
- Test individual agent initialization
- Test configuration loading
- Test prompt building
- Test output formatting

### Integration Tests
- Test pipeline execution
- Test agent communication
- Test error handling
- Test file output

### End-to-End Tests
- Test complete workflows
- Test with real APIs (optional)
- Test various topics
- Test all platforms

## Performance Characteristics

### Typical Execution Time
- Stage 1: 10-30 seconds (research with grounding)
- Stage 2: 10-20 seconds (draft writing)
- Stage 3: 5-10 seconds (review)
- Stage 4: 10-20 seconds (rewrite)
- Stage 5: 5-10 seconds (polish)
- Stage 6: 5-10 seconds (final check)

**Total:** 45-100 seconds per topic

### API Costs (Approximate)
- Gemini: $0.01-0.05 per request
- Claude: $0.02-0.10 per request
- Kimi: $0.01-0.03 per request

**Total:** $0.10-0.50 per complete pipeline

### Token Usage
- Research: ~8000 tokens
- Draft: ~4000 tokens
- Review: ~4000 tokens
- Revision: ~4000 tokens
- Polish: ~4000 tokens
- Check: ~2000 tokens

**Total:** ~26,000 tokens per pipeline

## Monitoring and Logging

### Current Logging
- Stage start/completion
- Error messages
- Configuration status
- CLI output

### Future Enhancements
- Structured logging
- Performance metrics
- API usage tracking
- Error analytics
- Quality metrics

## Deployment Options

### Local Development
```bash
python3 -m cligod.cli create "Topic"
```

### Containerized
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "cligod.cli"]
```

### Cloud Functions
- AWS Lambda
- Google Cloud Functions
- Azure Functions

### CI/CD Integration
- GitHub Actions
- GitLab CI
- Jenkins

## Future Enhancements

1. **Web Interface**
   - React/Vue frontend
   - REST API backend
   - Real-time stage visualization

2. **Batch Processing**
   - Process multiple topics
   - Parallel execution
   - Progress tracking

3. **Analytics Dashboard**
   - Usage statistics
   - Quality metrics
   - Cost tracking

4. **Agent Training**
   - Fine-tune personas
   - Learn from feedback
   - Improve over time

5. **Multi-Language Support**
   - Support multiple languages
   - Localized agents
   - Translation pipeline

---

This architecture provides a solid foundation for multi-agent content creation with clear separation of concerns and extensibility.
