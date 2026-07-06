"""
ConversationAnalyzer - Core analysis engine for Phase 1
Determines if GenerativeAgent can automate a conversation
"""

import json
import logging
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class Gap:
    """Represents a capability gap"""
    action: str
    gap_type: str  # 'missing_knowledge' | 'missing_api' | 'missing_tool'
    reason: str
    specific_knowledge: str = ""
    affected_task: str = ""
    suggested_fix: str = ""
    confidence: float = 0.8


@dataclass
class RecommendedImprovement:
    """A recommended improvement to enable automation"""
    improvement_type: str  # 'task_instruction_update' | 'kb_article' | 'api_enhancement'
    location: str  # GACS path where improvement should go
    priority: str  # 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW'
    description: str
    estimated_conversations_affected: int = 1
    estimated_implementation_hours: float = 1.0


@dataclass
class AnalysisResult:
    """Result of analyzing a single conversation"""
    conversation_id: str
    company_marker: str
    branch: str
    generative_agent: str  # 'yes' | 'no'
    category: str  # 'AUTOMATABLE' | 'MISSING_KNOWLEDGE' | 'MISSING_APIS' | 'APPROPRIATE_ESCALATION'
    missing_actions: List[Gap] = field(default_factory=list)
    recommended_improvements: List[RecommendedImprovement] = field(default_factory=list)
    available_functions: List[str] = field(default_factory=list)
    available_kb_articles: List[str] = field(default_factory=list)
    confidence: float = 0.8
    analysis_timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + 'Z')

    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'conversation_id': self.conversation_id,
            'company_marker': self.company_marker,
            'branch': self.branch,
            'generative_agent': self.generative_agent,
            'category': self.category,
            'missing_actions': [asdict(action) for action in self.missing_actions],
            'recommended_improvements': [asdict(imp) for imp in self.recommended_improvements],
            'available_resources': {
                'functions_available': self.available_functions,
                'kb_articles_available': self.available_kb_articles
            },
            'confidence': self.confidence,
            'analysis_timestamp': self.analysis_timestamp
        }


class ConversationAnalyzer:
    """
    Analyzes a single conversation to determine if GenAgent can automate it.

    Process:
    1. Fetch conversation data from Athena
    2. Fetch GenAgent task configuration from GACS
    3. Extract all agent actions from conversation
    4. Check feasibility of each action
    5. Classify conversation
    """

    def __init__(self, conversation_id: str, company_marker: str, branch_name: str = "main"):
        self.conv_id = conversation_id
        self.company = company_marker
        self.branch = branch_name

        # Will be populated during analysis
        self.conversation = None
        self.gacs_config = None
        self.agent_actions = []
        self.gaps = []

        logger.info(f"Initialized analyzer for conversation {conversation_id} ({company_marker}/{branch_name})")

    async def analyze(self) -> AnalysisResult:
        """
        Main analysis workflow.

        Returns:
            AnalysisResult object with classification and recommendations
        """
        try:
            logger.info(f"Starting analysis of conversation {self.conv_id}")

            # Step 1: Fetch conversation
            await self._fetch_conversation()
            if not self.conversation:
                logger.error(f"Failed to fetch conversation {self.conv_id}")
                raise Exception(f"Could not fetch conversation {self.conv_id}")

            # Step 2: Fetch GenAgent config
            await self._fetch_gacs_config()
            if not self.gacs_config:
                logger.error(f"Failed to fetch GACS config for {self.company}/{self.branch}")
                raise Exception(f"Could not fetch GACS config")

            # Step 3: Extract agent actions
            self._extract_agent_actions()
            logger.info(f"Extracted {len(self.agent_actions)} agent actions")

            # Step 4: Check feasibility of each action
            self._check_action_feasibility()
            logger.info(f"Found {len(self.gaps)} capability gaps")

            # Step 5: Classify and generate recommendations
            result = self._classify_conversation()

            logger.info(f"Analysis complete. Classification: {result.generative_agent}")
            return result

        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}", exc_info=True)
            raise

    async def _fetch_conversation(self) -> None:
        """
        Fetch conversation from data-sampling MCP server.

        TODO: Implement actual MCP call to mcp__data-sampling__fetch_conversations_by_id
        For now, this is a placeholder that shows the expected structure.
        """
        # In actual implementation:
        # self.conversation = await mcp_client.mcp__data_sampling__fetch_conversations_by_id(
        #     company_marker=self.company,
        #     conversation_ids=[self.conv_id],
        #     include_human_agent_utterances=True,
        #     is_voice=True
        # )

        logger.debug(f"Fetching conversation {self.conv_id} for {self.company}")
        # Placeholder: would be populated by MCP server call
        self.conversation = {"model_input": {"actions": []}}

    async def _fetch_gacs_config(self) -> None:
        """
        Fetch GenAgent task configuration from GACS via MCP.

        Retrieves:
        - Available tasks in this branch
        - Available functions with signatures
        - Available KB articles

        TODO: Implement actual MCP calls to mcp__gacs__get_branch
        """
        # In actual implementation:
        # branch_data = await mcp_client.mcp__gacs__get_branch(
        #     company_marker=self.company,
        #     branch_name=self.branch
        # )

        logger.debug(f"Fetching GACS config {self.company}/{self.branch} via MCP")
        # Placeholder structure
        self.gacs_config = {
            'tasks': {},
            'functions': {},
            'kb_articles': {}
        }

    def _extract_agent_actions(self) -> None:
        """
        Parse conversation and extract all agent actions.

        Identifies:
        1. Bot/talker messages and what they communicated
        2. Function calls made
        3. Data retrieved from APIs
        4. Information provided to customer
        """
        if not self.conversation or 'model_input' not in self.conversation:
            logger.warning("Conversation structure invalid")
            return

        actions = self.conversation['model_input'].get('actions', [])
        current_task = None

        for i, action in enumerate(actions):
            action_type = action.get('type')

            # Track current task context
            if action_type == 'enter_task':
                current_task = action.get('task_name')
            elif action_type == 'exit_task':
                current_task = None

            # Extract bot messages
            elif action_type == 'message':
                message = action.get('message', {})
                sender = message.get('sender', '')
                text = message.get('text', '')
                source = action.get('source_system', '')

                # Track talker messages (what agent said to customer)
                if sender == 'bot' and source == 'voice_assistant':
                    self.agent_actions.append({
                        'type': 'communication',
                        'content': text,
                        'timestamp': action.get('timestamp'),
                        'task_context': current_task,
                        'action_index': i,
                        'source': source
                    })

            # Track function calls
            elif action_type == 'function_request':
                func_request = action.get('function_request', {})
                func_name = func_request.get('function_name')
                parameters = func_request.get('parameters', {})

                self.agent_actions.append({
                    'type': 'function_call',
                    'function': func_name,
                    'parameters': parameters,
                    'timestamp': action.get('timestamp'),
                    'task_context': current_task,
                    'action_index': i
                })

    def _check_action_feasibility(self) -> None:
        """
        For each agent action, determine if GenAgent can perform it.

        Checks:
        1. Is the function available in GACS?
        2. Is the knowledge in available KB articles?
        3. Is it common sense conversational knowledge?
        """
        for action in self.agent_actions:
            gap = None

            if action['type'] == 'function_call':
                gap = self._check_function_available(action)

            elif action['type'] == 'communication':
                gap = self._check_message_feasibility(action)

            if gap:
                self.gaps.append(gap)

    def _check_function_available(self, action: Dict) -> Optional[Gap]:
        """
        Check if function is available in GACS config.
        """
        func_name = action.get('function')

        if not self.gacs_config or 'functions' not in self.gacs_config:
            return None

        available_functions = self.gacs_config.get('functions', {})

        if func_name not in available_functions:
            return Gap(
                action=f"Call function: {func_name}",
                gap_type='missing_api',
                reason=f"Function '{func_name}' not available in GACS",
                affected_task=action.get('task_context', 'unknown'),
                suggested_fix=f"Add '{func_name}' function to GACS or use alternative API"
            )

        return None

    def _check_message_feasibility(self, action: Dict) -> Optional[Gap]:
        """
        Check if message content can come from available resources.

        NOTE: This is a simplified check. In production, would use LLM
        to assess if content requires knowledge not in KB.
        """
        message = action.get('content', '')
        task_context = action.get('task_context', '')

        # TODO: Implement LLM-based feasibility check using Claude
        # For now, return None (placeholder)
        #
        # In actual implementation:
        # - Parse message for domain-specific concepts
        # - Check if these concepts are in available KB articles
        # - Ask LLM to assess if missing knowledge is:
        #   a) In available KB articles
        #   b) Common sense knowledge
        #   c) Domain knowledge not available

        return None

    def _classify_conversation(self) -> AnalysisResult:
        """
        Classify the conversation based on identified gaps.

        Classification logic:
        - If no gaps: "yes" (automatable)
        - If gaps exist: categorize by type and mark as "no"
        """
        result = AnalysisResult(
            conversation_id=self.conv_id,
            company_marker=self.company,
            branch=self.branch,
            available_functions=list(self.gacs_config.get('functions', {}).keys()),
            available_kb_articles=list(self.gacs_config.get('kb_articles', {}).keys())
        )

        if not self.gaps:
            result.generative_agent = 'yes'
            result.category = 'AUTOMATABLE'
            result.confidence = 0.95
        else:
            result.generative_agent = 'no'
            result.missing_actions = self.gaps

            # Categorize gaps
            gap_types = set(gap.gap_type for gap in self.gaps)

            if 'missing_knowledge' in gap_types:
                result.category = 'MISSING_KNOWLEDGE'
            elif 'missing_api' in gap_types:
                result.category = 'MISSING_APIS'
            else:
                result.category = 'UNKNOWN'

            # Generate recommendations
            result.recommended_improvements = self._generate_recommendations()
            result.confidence = 0.85

        return result

    def _generate_recommendations(self) -> List[RecommendedImprovement]:
        """
        Generate specific recommendations to enable automation.
        """
        recommendations = []

        for gap in self.gaps:
            if gap.gap_type == 'missing_api':
                rec = RecommendedImprovement(
                    improvement_type='api_enhancement',
                    location=f"functions/{gap.action.split('/')[-1] if '/' in gap.action else 'new_function'}",
                    priority='HIGH',
                    description=f"Add or enhance API: {gap.suggested_fix}",
                    estimated_implementation_hours=8.0
                )
            else:
                rec = RecommendedImprovement(
                    improvement_type='task_instruction_update',
                    location=f"tasks/{gap.affected_task}/promptInstructions",
                    priority='HIGH',
                    description=f"Add knowledge about: {gap.specific_knowledge}",
                    estimated_implementation_hours=2.0
                )

            recommendations.append(rec)

        return recommendations


# Example usage
if __name__ == "__main__":
    import asyncio

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    async def main():
        analyzer = ConversationAnalyzer(
            conversation_id="3408138022-1698370033-2504114677-1773867395",
            company_marker="assurantauto",
            branch_name="main"
        )

        try:
            result = await analyzer.analyze()
            print(json.dumps(result.to_dict(), indent=2))
        except Exception as e:
            print(f"Analysis failed: {e}")

    asyncio.run(main())