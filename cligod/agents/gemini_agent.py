"""Gemini agent implementation."""

import os
from typing import Dict, Any, Optional
from .base import BaseAgent, AgentResponse

try:
    import google.generativeai as genai
    from google.cloud import aiplatform
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False


class GeminiAgent(BaseAgent):
    """Agent that uses Google's Gemini model."""
    
    def __init__(self, name: str, config: Dict[str, Any], api_key: Optional[str] = None,
                 use_vertex: bool = False, vertex_project_id: Optional[str] = None,
                 vertex_location: Optional[str] = None):
        """Initialize Gemini agent.
        
        Args:
            name: Agent name
            config: Agent configuration
            api_key: Gemini API key (for direct API)
            use_vertex: Whether to use Vertex AI
            vertex_project_id: Vertex AI project ID
            vertex_location: Vertex AI location
        """
        super().__init__(name, config, api_key)
        
        if not GOOGLE_AVAILABLE:
            raise ImportError("google-generativeai and google-cloud-aiplatform are required for GeminiAgent")
        
        self.use_vertex = use_vertex or config.get('use_grounding', False)
        self.use_grounding = config.get('use_grounding', False)
        
        if self.use_vertex:
            # Initialize Vertex AI
            if vertex_project_id and vertex_location:
                aiplatform.init(project=vertex_project_id, location=vertex_location)
            self.client = None  # Will use Vertex AI SDK
        else:
            # Initialize regular Gemini API
            if api_key:
                genai.configure(api_key=api_key)
            self.client = genai
    
    def generate(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Generate content using Gemini.
        
        Args:
            prompt: The prompt to send to Gemini
            context: Optional context from previous stages
        
        Returns:
            Generated text response
        """
        full_prompt = self._build_system_prompt(prompt)
        
        try:
            if self.use_vertex:
                return self._generate_vertex(full_prompt)
            else:
                return self._generate_api(full_prompt)
        except Exception as e:
            return f"Error generating content with {self.name}: {str(e)}"
    
    def _generate_api(self, prompt: str) -> str:
        """Generate using Gemini API.
        
        Args:
            prompt: The prompt
        
        Returns:
            Generated content
        """
        model = self.client.GenerativeModel(
            model_name=self.model,
            generation_config={
                'temperature': self.temperature,
                'max_output_tokens': self.max_tokens,
            }
        )
        
        response = model.generate_content(prompt)
        return response.text
    
    def _generate_vertex(self, prompt: str) -> str:
        """Generate using Vertex AI with optional grounding.
        
        Args:
            prompt: The prompt
        
        Returns:
            Generated content
        """
        from vertexai.preview.generative_models import GenerativeModel, Tool
        from vertexai.preview import grounding
        
        tools = []
        if self.use_grounding:
            # Enable Google Search grounding
            tools.append(Tool.from_google_search_retrieval(grounding.GoogleSearchRetrieval()))
        
        model = GenerativeModel(
            model_name=self.model,
            tools=tools if tools else None
        )
        
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': self.temperature,
                'max_output_tokens': self.max_tokens,
            }
        )
        
        return response.text
