"""Base agent class for LLM interactions."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List


class BaseAgent(ABC):
    """Base class for all LLM agents."""
    
    def __init__(self, name: str, config: Dict[str, Any], api_key: Optional[str] = None):
        """Initialize agent.
        
        Args:
            name: Agent name
            config: Agent configuration from config.yaml
            api_key: API key for the LLM provider
        """
        self.name = name
        self.config = config
        self.api_key = api_key
        self.model = config.get('model', 'default')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 4000)
        self.persona = config.get('persona', '')
    
    @abstractmethod
    def generate(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Generate content using the LLM.
        
        Args:
            prompt: The prompt to send to the LLM
            context: Optional context from previous stages
        
        Returns:
            Generated text response
        """
        pass
    
    def _build_system_prompt(self, task_prompt: str) -> str:
        """Build complete system prompt with persona.
        
        Args:
            task_prompt: Specific task prompt
        
        Returns:
            Complete prompt with persona and task
        """
        return f"{self.persona}\n\n{task_prompt}"


class AgentResponse:
    """Structured response from an agent."""
    
    def __init__(self, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Initialize agent response.
        
        Args:
            content: The main content generated
            metadata: Additional metadata (sources, tokens used, etc.)
        """
        self.content = content
        self.metadata = metadata or {}
    
    def __str__(self) -> str:
        return self.content
