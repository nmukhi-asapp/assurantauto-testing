"""
GenAgent Capability Analyzer - Phase 1 Core Engine

This module implements single-conversation analysis to determine if GenerativeAgent
can automate a conversation based on available tools and knowledge.

Main Components:
- ConversationAnalyzer: Orchestrates the analysis workflow
- Gap: Represents a capability gap (missing tool or knowledge)
- AnalysisResult: Result of analyzing a conversation
"""

from analyzer import (
    ConversationAnalyzer,
    Gap,
    AnalysisResult,
    RecommendedImprovement
)

__all__ = [
    'ConversationAnalyzer',
    'Gap',
    'AnalysisResult',
    'RecommendedImprovement'
]

__version__ = '0.1.0'
__status__ = 'Phase 1 - In Development'