#!/usr/bin/env python3
"""Test script to verify CLIgod installation and basic functionality."""

import sys
import os

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    try:
        from cligod import __version__
        print(f"✅ CLIgod version: {__version__}")
        
        from cligod.config import Config
        print("✅ Config module loaded")
        
        from cligod.agents import BaseAgent, GeminiAgent, ClaudeAgent, KimiAgent
        print("✅ Agent modules loaded")
        
        from cligod.pipeline import ContentPipeline
        print("✅ Pipeline module loaded")
        
        from cligod.cli import cli
        print("✅ CLI module loaded")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """Test configuration loading."""
    print("\nTesting configuration...")
    try:
        from cligod.config import Config
        config = Config()
        
        # Check if config loaded
        if hasattr(config, 'config'):
            print("✅ Config loaded successfully")
            
            # Check for agent configs
            agents = ['gemini_research', 'gemini_writer', 'claude_reviewer', 
                     'claude_checker', 'gemini_rewriter', 'kimi_polisher']
            for agent in agents:
                if agent in config.config.get('agents', {}):
                    print(f"✅ Agent config found: {agent}")
                else:
                    print(f"⚠️  Agent config missing: {agent}")
            
            return True
        else:
            print("❌ Config not loaded properly")
            return False
            
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_api_keys():
    """Test API key configuration."""
    print("\nTesting API key configuration...")
    try:
        from cligod.config import Config
        config = Config()
        
        keys = {
            'Gemini': config.gemini_api_key,
            'Claude': config.claude_api_key,
            'Kimi': config.kimi_api_key
        }
        
        all_set = True
        for name, key in keys.items():
            if key and key != 'your-gemini-api-key-here' and key != 'your-claude-api-key-here' and key != 'your-kimi-api-key-here':
                print(f"✅ {name} API key is set")
            else:
                print(f"⚠️  {name} API key not configured")
                all_set = False
        
        return all_set
        
    except Exception as e:
        print(f"❌ API key check error: {e}")
        return False

def test_agent_initialization():
    """Test agent initialization (without making API calls)."""
    print("\nTesting agent initialization...")
    try:
        from cligod.config import Config
        from cligod.agents import GeminiAgent, ClaudeAgent, KimiAgent
        
        config = Config()
        
        # Try to initialize agents (will fail if API keys are invalid)
        try:
            gemini_config = config.get_agent_config('gemini_research')
            gemini = GeminiAgent(
                'test_gemini',
                gemini_config,
                api_key=config.gemini_api_key
            )
            print("✅ GeminiAgent initialized")
        except Exception as e:
            print(f"⚠️  GeminiAgent initialization: {e}")
        
        try:
            claude_config = config.get_agent_config('claude_reviewer')
            if config.claude_api_key:
                claude = ClaudeAgent(
                    'test_claude',
                    claude_config,
                    api_key=config.claude_api_key
                )
                print("✅ ClaudeAgent initialized")
        except Exception as e:
            print(f"⚠️  ClaudeAgent initialization: {e}")
        
        try:
            kimi_config = config.get_agent_config('kimi_polisher')
            if config.kimi_api_key:
                kimi = KimiAgent(
                    'test_kimi',
                    kimi_config,
                    api_key=config.kimi_api_key
                )
                print("✅ KimiAgent initialized")
        except Exception as e:
            print(f"⚠️  KimiAgent initialization: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Agent initialization error: {e}")
        return False

def main():
    """Run all tests."""
    print("="*60)
    print("CLIgod Installation and Configuration Test")
    print("="*60)
    
    results = []
    
    results.append(("Module Imports", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("API Keys", test_api_keys()))
    results.append(("Agent Initialization", test_agent_initialization()))
    
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{name}: {status}")
        if not passed:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n✅ All tests passed! CLIgod is ready to use.")
        print("\nNext steps:")
        print("  1. Run: python3 -m cligod.cli check-config")
        print('  2. Run: python3 -m cligod.cli create "Your topic here"')
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the configuration.")
        print("\nTroubleshooting:")
        print("  1. Make sure .env file exists and has valid API keys")
        print("  2. Install missing dependencies: pip install -r requirements.txt")
        print("  3. Check config.yaml for proper agent configurations")
        return 1

if __name__ == '__main__':
    sys.exit(main())
