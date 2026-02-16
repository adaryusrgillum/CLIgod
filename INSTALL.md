# Installation Guide for CLIgod

This guide will help you install and configure CLIgod on your system.

## System Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)
- Active internet connection
- API keys for Gemini, Claude, and Kimi

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/adaryusrgillum/CLIgod.git
cd CLIgod
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

### 4. Configure API Keys

#### Option A: Using the Init Command

```bash
python3 -m cligod.cli init
```

This creates a `.env` file. Then edit it with your API keys:

```bash
nano .env  # or use your preferred editor
```

#### Option B: Manual Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```bash
# Gemini API Configuration
GEMINI_API_KEY=your-actual-gemini-key

# Claude API Configuration
CLAUDE_API_KEY=your-actual-claude-key

# Kimi API Configuration
KIMI_API_KEY=your-actual-kimi-key

# Vertex AI (Optional - for Google Search grounding)
VERTEX_PROJECT_ID=your-gcp-project-id
VERTEX_LOCATION=us-east5
VERTEX_ACCESS_TOKEN=your-vertex-token
```

### 5. Verify Installation

Run the test script:

```bash
python3 test_installation.py
```

Or check configuration:

```bash
python3 -m cligod.cli check-config
```

You should see:

```
🔍 Configuration Status

API Keys:
  Gemini API Key: ✅ Set
  Claude API Key: ✅ Set
  Kimi API Key: ✅ Set
...
```

## Getting API Keys

### Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key"
4. Copy the key to your `.env` file

### Claude API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign in or create an account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-ant-`)

### Kimi API Key

1. Go to [Moonshot AI Platform](https://platform.moonshot.cn/)
2. Sign in or register
3. Navigate to API section
4. Create a new API key
5. Copy the key (starts with `sk-kimi-`)

## Optional: Vertex AI Setup (for Google Search Grounding)

If you want to use Google Search grounding in Stage 1 (RESEARCH), set up Vertex AI:

### Install Google Cloud SDK

```bash
# On Linux:
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# On Mac:
brew install google-cloud-sdk

# On Windows:
# Download from https://cloud.google.com/sdk/docs/install
```

### Configure Vertex AI

```bash
# Authenticate
gcloud auth application-default login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

# Get access token
gcloud auth application-default print-access-token
```

Add to `.env`:

```bash
VERTEX_PROJECT_ID=your-actual-project-id
VERTEX_LOCATION=us-east5
VERTEX_ACCESS_TOKEN=your-actual-token
```

## Optional: Corporate Proxy Configuration

If you're behind a corporate proxy:

```bash
# Add to .env
HTTP_PROXY=http://your-proxy:port
HTTPS_PROXY=https://your-proxy:port

# For Vertex AI routing
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id
```

## Verification

### Test Basic Functionality

```bash
# Show help
python3 -m cligod.cli --help

# Check configuration
python3 -m cligod.cli check-config

# Initialize if needed
python3 -m cligod.cli init
```

### Run a Test Query (Optional)

**Note**: This will consume API credits!

```bash
python3 -m cligod.cli create "Test topic" --output test-output.json
```

If successful, you'll see output from all 6 pipeline stages.

## Troubleshooting

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'dotenv'`

**Solution**:
```bash
pip install python-dotenv
# Or reinstall all dependencies
pip install -r requirements.txt
```

### API Key Errors

**Problem**: `Error: GEMINI_API_KEY not set in environment`

**Solution**:
- Ensure `.env` file exists in the current directory
- Check that API keys are properly formatted (no extra spaces)
- Try setting environment variables directly:
  ```bash
  export GEMINI_API_KEY=your-key
  export CLAUDE_API_KEY=your-key
  export KIMI_API_KEY=your-key
  ```

### Vertex AI Errors

**Problem**: `Could not automatically determine credentials`

**Solution**:
```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

### Permission Errors

**Problem**: `Permission denied` when installing packages

**Solution**:
```bash
# Use user installation
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Missing Dependencies

**Problem**: Some packages fail to install

**Solution**:
```bash
# Update pip
pip install --upgrade pip

# Install specific packages individually
pip install google-cloud-aiplatform
pip install anthropic
pip install requests
```

## Platform-Specific Notes

### Linux/Ubuntu

```bash
# Install Python development headers if needed
sudo apt-get update
sudo apt-get install python3-dev python3-pip

# Install CLIgod
pip3 install -r requirements.txt
```

### macOS

```bash
# Install Python if needed
brew install python3

# Install CLIgod
pip3 install -r requirements.txt
```

### Windows

```powershell
# Use PowerShell or Command Prompt
python -m pip install -r requirements.txt

# Set environment variables (PowerShell)
$env:GEMINI_API_KEY="your-key"
$env:CLAUDE_API_KEY="your-key"
$env:KIMI_API_KEY="your-key"
```

## Development Installation

If you want to contribute or modify CLIgod:

```bash
# Clone repository
git clone https://github.com/adaryusrgillum/CLIgod.git
cd CLIgod

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in editable mode
pip install -e .

# Install development dependencies (if any)
pip install -r requirements-dev.txt  # if exists
```

## Uninstallation

```bash
# If installed with pip install -e .
pip uninstall cligod

# Remove virtual environment
deactivate
rm -rf venv

# Remove configuration (optional)
rm .env
```

## Next Steps

After successful installation:

1. ✅ Review the [README.md](README.md) for usage examples
2. ✅ Check [examples/README.md](examples/README.md) for sample commands
3. ✅ Try creating your first content:
   ```bash
   python3 -m cligod.cli create "Your Topic" --verbose
   ```
4. ✅ Read the full documentation to understand the 6-stage pipeline

## Support

If you encounter issues:

1. Check this guide's troubleshooting section
2. Run `python3 test_installation.py` to identify problems
3. Open an issue on GitHub with:
   - Python version: `python3 --version`
   - Operating system
   - Error message
   - Steps to reproduce

## Security Notes

⚠️ **Important**:
- Never commit `.env` files to version control
- Keep your API keys secure
- Don't share your API keys
- Use environment-specific configurations for different deployments
- Consider using a secret management service in production

---

**Congratulations!** You're now ready to use CLIgod for multi-agent content creation! 🚀
