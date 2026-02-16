"""Claude agent implementation."""

from typing import Dict, Any, Optional
from .base import BaseAgent, AgentResponse

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


class ClaudeAgent(BaseAgent):
    """Agent that uses Anthropic's Claude model."""
    
    def __init__(self, name: str, config: Dict[str, Any], api_key: Optional[str] = None):
        """Initialize Claude agent.
        
        Args:
            name: Agent name
            config: Agent configuration
            api_key: Claude API key
        """
        super().__init__(name, config, api_key)
        
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic is required for ClaudeAgent")
        
        if not api_key:
            raise ValueError("Claude API key is required")
        
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def generate(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Generate content using Claude.
        
        Args:
            prompt: The prompt to send to Claude
            context: Optional context from previous stages
        
        Returns:
            Generated text response
        """
        full_prompt = self._build_system_prompt(prompt)
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self.persona,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            return message.content[0].text
        except Exception as e:
            return f"Error generating content with {self.name}: {str(e)}"
