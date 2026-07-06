"""
Unit tests for ConversationAnalyzer (Phase 1 core engine)
"""

import pytest
import json
from analyzer import ConversationAnalyzer, Gap, AnalysisResult


class TestGapDataclass:
    """Test Gap data structure"""

    def test_gap_creation(self):
        gap = Gap(
            action="Call getClaimsLast8OfVin",
            gap_type="missing_api",
            reason="Function not available",
            specific_knowledge="",
            affected_task="RepairShopIssues"
        )
        assert gap.action == "Call getClaimsLast8OfVin"
        assert gap.gap_type == "missing_api"
        assert gap.reason == "Function not available"

    def test_gap_with_optional_fields(self):
        gap = Gap(
            action="Interpret claim status",
            gap_type="missing_knowledge",
            reason="No KB article",
            specific_knowledge="Payment status mapping rules",
            confidence=0.92
        )
        assert gap.confidence == 0.92


class TestAnalysisResult:
    """Test AnalysisResult data structure and serialization"""

    def test_analysis_result_creation(self):
        result = AnalysisResult(
            conversation_id="test_conv_001",
            company_marker="assurantauto",
            branch="main",
            generative_agent="yes",
            category="AUTOMATABLE"
        )
        assert result.conversation_id == "test_conv_001"
        assert result.generative_agent == "yes"

    def test_analysis_result_to_dict(self):
        result = AnalysisResult(
            conversation_id="test_conv_001",
            company_marker="assurantauto",
            branch="main",
            generative_agent="no",
            category="MISSING_KNOWLEDGE",
            missing_actions=[
                Gap(
                    action="Interpret status",
                    gap_type="missing_knowledge",
                    reason="No KB"
                )
            ]
        )

        result_dict = result.to_dict()
        assert result_dict['conversation_id'] == "test_conv_001"
        assert result_dict['generative_agent'] == "no"
        assert len(result_dict['missing_actions']) == 1
        assert 'analysis_timestamp' in result_dict


class TestConversationAnalyzer:
    """Test ConversationAnalyzer core functionality"""

    def test_analyzer_initialization(self):
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto",
            branch_name="main"
        )
        assert analyzer.conv_id == "test_conv_001"
        assert analyzer.company == "assurantauto"
        assert analyzer.branch == "main"

    @pytest.mark.asyncio
    async def test_fetch_conversation_placeholder(self):
        """Test that conversation fetch initializes structure"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )
        await analyzer._fetch_conversation()
        # Placeholder implementation should create structure
        assert analyzer.conversation is not None
        assert 'model_input' in analyzer.conversation

    @pytest.mark.asyncio
    async def test_fetch_gacs_config_placeholder(self):
        """Test that GACS config fetch initializes structure"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )
        await analyzer._fetch_gacs_config()
        # Placeholder implementation should create structure
        assert analyzer.gacs_config is not None
        assert 'tasks' in analyzer.gacs_config
        assert 'functions' in analyzer.gacs_config

    def test_extract_agent_actions_empty(self):
        """Test extraction with empty conversation"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )
        analyzer.conversation = {"model_input": {"actions": []}}

        analyzer._extract_agent_actions()
        assert len(analyzer.agent_actions) == 0

    def test_extract_agent_actions_with_messages(self):
        """Test extraction of bot messages"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )

        analyzer.conversation = {
            "model_input": {
                "actions": [
                    {
                        "type": "message",
                        "message": {
                            "sender": "bot",
                            "text": "Hello, how can I help?"
                        },
                        "source_system": "voice_assistant",
                        "timestamp": "2026-06-19T00:00:00Z"
                    }
                ]
            }
        }

        analyzer._extract_agent_actions()
        assert len(analyzer.agent_actions) == 1
        assert analyzer.agent_actions[0]['type'] == 'communication'
        assert "Hello" in analyzer.agent_actions[0]['content']

    def test_extract_agent_actions_with_function_calls(self):
        """Test extraction of function calls"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )

        analyzer.conversation = {
            "model_input": {
                "actions": [
                    {
                        "type": "function_request",
                        "function_request": {
                            "function_name": "getClaimsLast8OfVin",
                            "parameters": {"vin": "RB004888"}
                        },
                        "timestamp": "2026-06-19T00:00:00Z"
                    }
                ]
            }
        }

        analyzer._extract_agent_actions()
        assert len(analyzer.agent_actions) == 1
        assert analyzer.agent_actions[0]['type'] == 'function_call'
        assert analyzer.agent_actions[0]['function'] == 'getClaimsLast8OfVin'

    def test_check_function_available_found(self):
        """Test when function is available"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )

        analyzer.gacs_config = {
            'functions': {
                'getClaimsLast8OfVin': {'signature': '...'},
                'is_repair_facility': {'signature': '...'}
            }
        }

        action = {
            'type': 'function_call',
            'function': 'getClaimsLast8OfVin'
        }

        gap = analyzer._check_function_available(action)
        assert gap is None

    def test_check_function_available_not_found(self):
        """Test when function is not available"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )

        analyzer.gacs_config = {
            'functions': {
                'getClaimsLast8OfVin': {'signature': '...'}
            }
        }

        action = {
            'type': 'function_call',
            'function': 'unknownFunction'
        }

        gap = analyzer._check_function_available(action)
        assert gap is not None
        assert gap.gap_type == 'missing_api'
        assert 'unknownFunction' in gap.reason

    @pytest.mark.asyncio
    async def test_classify_no_gaps(self):
        """Test classification when no gaps found"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )
        analyzer.conversation = {"model_input": {"actions": []}}
        analyzer.gacs_config = {'functions': {}, 'kb_articles': {}, 'tasks': {}}
        analyzer.gaps = []

        result = analyzer._classify_conversation()
        assert result.generative_agent == 'yes'
        assert result.category == 'AUTOMATABLE'

    @pytest.mark.asyncio
    async def test_classify_with_knowledge_gap(self):
        """Test classification with knowledge gaps"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )
        analyzer.conversation = {"model_input": {"actions": []}}
        analyzer.gacs_config = {'functions': {}, 'kb_articles': {}, 'tasks': {}}
        analyzer.gaps = [
            Gap(
                action="Interpret status",
                gap_type="missing_knowledge",
                reason="No KB article"
            )
        ]

        result = analyzer._classify_conversation()
        assert result.generative_agent == 'no'
        assert result.category == 'MISSING_KNOWLEDGE'

    @pytest.mark.asyncio
    async def test_classify_with_api_gap(self):
        """Test classification with API gaps"""
        analyzer = ConversationAnalyzer(
            conversation_id="test_conv_001",
            company_marker="assurantauto"
        )
        analyzer.conversation = {"model_input": {"actions": []}}
        analyzer.gacs_config = {'functions': {}, 'kb_articles': {}, 'tasks': {}}
        analyzer.gaps = [
            Gap(
                action="Call function",
                gap_type="missing_api",
                reason="Function not available"
            )
        ]

        result = analyzer._classify_conversation()
        assert result.generative_agent == 'no'
        assert result.category == 'MISSING_APIS'


# Integration tests (require actual MCP connections)
class TestConversationAnalyzerIntegration:
    """Integration tests with real conversation data"""

    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires MCP server access")
    async def test_analyze_real_conversation(self):
        """Test analyzing real assurantauto conversation"""
        analyzer = ConversationAnalyzer(
            conversation_id="3408138022-1698370033-2504114677-1773867395",
            company_marker="assurantauto",
            branch_name="main"
        )

        result = await analyzer.analyze()
        assert result is not None
        assert result.conversation_id == "3408138022-1698370033-2504114677-1773867395"
        assert result.generative_agent in ['yes', 'no']
        assert result.category is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])