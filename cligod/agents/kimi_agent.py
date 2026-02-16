"""Kimi agent implementation."""

from typing import Dict, Any, Optional
import requests
from .base import BaseAgent, AgentResponse


class KimiAgent(BaseAgent):
    """Agent that uses Kimi (Moonshot AI) model."""
    
    def __init__(self, name: str, config: Dict[str, Any], api_key: Optional[str] = None):
        """Initialize Kimi agent.
        
        Args:
            name: Agent name
            config: Agent configuration
            api_key: Kimi API key
        """
        super().__init__(name, config, api_key)
        
        if not api_key:
            raise ValueError("Kimi API key is required")
        
        self.api_endpoint = "https://api.moonshot.cn/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def generate(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Generate content using Kimi.
        
        Args:
            prompt: The prompt to send to Kimi
            context: Optional context from previous stages
        
        Returns:
            Generated text response
        """
        full_prompt = self._build_system_prompt(prompt)
        
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": self.persona
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens
            }
            
            response = requests.post(
                self.api_endpoint,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
        except Exception as e:
            return f"Error generating content with {self.name}: {str(e)}"
