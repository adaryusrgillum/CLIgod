"""Pipeline orchestrator for the 6-stage content creation process."""

import logging
from typing import Dict, Any, Optional, List
from datetime import datetime

from .agents import GeminiAgent, ClaudeAgent, KimiAgent
from .config import Config


class ContentPipeline:
    """Orchestrates the 6-stage multi-agent content creation pipeline."""
    
    def __init__(self, config: Config):
        """Initialize the pipeline.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Initialize agents
        self._init_agents()
        
        # Pipeline state
        self.pipeline_state = {
            'research': None,
            'draft': None,
            'review': None,
            'revision': None,
            'polish': None,
            'final_check': None
        }
    
    def _init_agents(self):
        """Initialize all agents for the pipeline."""
        # Stage 1: Research (Gemini with grounding)
        self.research_agent = GeminiAgent(
            name='gemini_research',
            config=self.config.get_agent_config('gemini_research'),
            api_key=self.config.gemini_api_key,
            use_vertex=True,
            vertex_project_id=self.config.vertex_project_id,
            vertex_location=self.config.vertex_location
        )
        
        # Stage 2 & 4: Write/Rewrite (Gemini)
        self.writer_agent = GeminiAgent(
            name='gemini_writer',
            config=self.config.get_agent_config('gemini_writer'),
            api_key=self.config.gemini_api_key
        )
        
        self.rewriter_agent = GeminiAgent(
            name='gemini_rewriter',
            config=self.config.get_agent_config('gemini_rewriter'),
            api_key=self.config.gemini_api_key
        )
        
        # Stage 3 & 6: Review/Final Check (Claude)
        self.reviewer_agent = ClaudeAgent(
            name='claude_reviewer',
            config=self.config.get_agent_config('claude_reviewer'),
            api_key=self.config.claude_api_key
        )
        
        self.checker_agent = ClaudeAgent(
            name='claude_checker',
            config=self.config.get_agent_config('claude_checker'),
            api_key=self.config.claude_api_key
        )
        
        # Stage 5: Polish (Kimi)
        self.polisher_agent = KimiAgent(
            name='kimi_polisher',
            config=self.config.get_agent_config('kimi_polisher'),
            api_key=self.config.kimi_api_key
        )
    
    def run(self, topic: str, citation_style: str = 'APA', 
            target_platform: Optional[str] = None) -> Dict[str, Any]:
        """Run the complete 6-stage pipeline.
        
        Args:
            topic: The topic to create content about
            citation_style: Citation style (APA or MLA)
            target_platform: Target social media platform
        
        Returns:
            Dictionary containing all pipeline outputs
        """
        self.logger.info(f"Starting pipeline for topic: {topic}")
        
        # Stage 1: Research
        self.logger.info("Stage 1: RESEARCH (Gemini with grounding)")
        research = self.stage1_research(topic, citation_style)
        self.pipeline_state['research'] = research
        
        # Stage 2: Write
        self.logger.info("Stage 2: WRITE (Gemini)")
        draft = self.stage2_write(topic, research, citation_style, target_platform)
        self.pipeline_state['draft'] = draft
        
        # Stage 3: Review
        self.logger.info("Stage 3: REVIEW (Claude)")
        review = self.stage3_review(draft, citation_style, target_platform)
        self.pipeline_state['review'] = review
        
        # Stage 4: Rewrite
        self.logger.info("Stage 4: REWRITE (Gemini)")
        revision = self.stage4_rewrite(draft, review, citation_style)
        self.pipeline_state['revision'] = revision
        
        # Stage 5: Polish
        self.logger.info("Stage 5: POLISH (Kimi)")
        polished = self.stage5_polish(revision)
        self.pipeline_state['polish'] = polished
        
        # Stage 6: Final Check
        self.logger.info("Stage 6: FINAL CHECK (Claude)")
        final_check = self.stage6_final_check(polished, citation_style, target_platform)
        self.pipeline_state['final_check'] = final_check
        
        return {
            'topic': topic,
            'citation_style': citation_style,
            'target_platform': target_platform,
            'timestamp': datetime.now().isoformat(),
            'stages': self.pipeline_state,
            'final_content': polished,
            'passed_quality_gate': self._parse_pass_fail(final_check)
        }
    
    def stage1_research(self, topic: str, citation_style: str) -> str:
        """Stage 1: Deep research with grounding."""
        prompt = f"""
Conduct deep, comprehensive research on the following topic: {topic}

Your research should:
1. Identify current trends and recent developments
2. Find credible, authoritative sources
3. Extract key insights, statistics, and facts
4. Note important quotes and citations
5. Identify SEO keywords and trending hashtags
6. Consider the target audience for social media

Please use Google Search grounding to find the most current and relevant information.
Organize your findings in a structured format with proper citations in {citation_style} style.
"""
        return self.research_agent.generate(prompt)
    
    def stage2_write(self, topic: str, research: str, citation_style: str, 
                     target_platform: Optional[str]) -> str:
        """Stage 2: Write first draft."""
        platform_note = f" for {target_platform}" if target_platform else " for social media"
        
        prompt = f"""
Based on the following research, write an engaging, informative article{platform_note}:

RESEARCH:
{research}

TOPIC: {topic}

Your article should:
1. Be engaging and accessible while maintaining accuracy
2. Include proper citations in {citation_style} format
3. Be optimized for SEO with natural keyword integration
4. Include relevant hashtags
5. Have a clear structure with introduction, body, and conclusion
6. Be suitable for social media sharing
7. Include a compelling hook and call-to-action

Write a complete draft now.
"""
        return self.writer_agent.generate(prompt)
    
    def stage3_review(self, draft: str, citation_style: str, 
                      target_platform: Optional[str]) -> str:
        """Stage 3: Critical review."""
        platform_note = f" for {target_platform}" if target_platform else " for social media"
        
        prompt = f"""
Review the following content{platform_note} and provide critical, actionable feedback:

CONTENT:
{draft}

Evaluate:
1. Clarity and readability
2. Accuracy and factual correctness
3. Citation quality and format ({citation_style} style)
4. SEO optimization (keyword usage, meta description potential)
5. Social media engagement potential
6. Structure and flow
7. Grammar, spelling, and style
8. Call-to-action effectiveness

Provide specific, actionable feedback for improvement. Be thorough but constructive.
"""
        return self.reviewer_agent.generate(prompt)
    
    def stage4_rewrite(self, draft: str, review: str, citation_style: str) -> str:
        """Stage 4: Rewrite incorporating feedback."""
        prompt = f"""
Revise the following content based on the editorial feedback provided:

ORIGINAL DRAFT:
{draft}

EDITORIAL FEEDBACK:
{review}

Instructions:
1. Address all valid criticisms from the review
2. Maintain the core message and facts
3. Improve clarity, engagement, and SEO
4. Ensure citations are properly formatted in {citation_style} style
5. Enhance social media appeal
6. Fix any errors noted

Provide the complete revised version.
"""
        return self.rewriter_agent.generate(prompt)
    
    def stage5_polish(self, content: str) -> str:
        """Stage 5: Polish for flow and readability."""
        prompt = f"""
Polish the following content for optimal flow, readability, and engagement:

CONTENT:
{content}

Focus on:
1. Smooth transitions between sections
2. Natural, conversational tone
3. Varied sentence structure
4. Rhythm and pacing
5. Reader engagement
6. Clarity and conciseness

Preserve all facts, citations, and key messages while enhancing readability.
Provide the polished final version.
"""
        return self.polisher_agent.generate(prompt)
    
    def stage6_final_check(self, content: str, citation_style: str,
                           target_platform: Optional[str]) -> str:
        """Stage 6: Quality gate check."""
        platform_note = f" for {target_platform}" if target_platform else " for social media"
        
        prompt = f"""
Perform a final quality check on this content{platform_note}:

CONTENT:
{content}

Evaluate against these criteria:
1. Accuracy and factual correctness
2. Clarity and readability
3. Engagement potential
4. Proper citations ({citation_style} format)
5. SEO optimization
6. Social media readiness
7. Professional quality

Provide a PASS or FAIL decision with brief justification.
If FAIL, list the critical issues that must be addressed.
"""
        return self.checker_agent.generate(prompt)
    
    def _parse_pass_fail(self, final_check: str) -> bool:
        """Parse the PASS/FAIL decision from final check.
        
        Args:
            final_check: Final check response
        
        Returns:
            True if PASS, False if FAIL
        """
        check_upper = final_check.upper()
        if 'PASS' in check_upper and 'FAIL' not in check_upper:
            return True
        return False
