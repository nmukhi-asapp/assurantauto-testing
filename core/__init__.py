"""
Core infrastructure module for generative-agent-optimization-mcp.

This module provides shared utilities, logging, constants, and validation
following SOLID and DRY principles to eliminate code duplication across
the repository.
"""

from .constants import (
    DEFAULT_TEMPERATURE,
    MIN_TEMPERATURE,
    MAX_TEMPERATURE,
    DEFAULT_LOG_LEVEL,
    DEFAULT_MCP_LOG_LEVEL,
    LOG_LEVELS,
    DEFAULT_COUNT,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_METRICS,
    DEFAULT_VERBOSE,
    DEFAULT_EVAL_ONLY,
    DEFAULT_OUTPUT_DIR,
    DEFAULT_SAMPLED_CONVOS_DIR,
    DEFAULT_RESULTS_DIR,
    DATE_FORMAT,
    TIMESTAMP_FORMAT,
    DATETIME_FORMAT,
    ERROR_MESSAGES,
    SUCCESS_MESSAGES,
    # Voice-specific constants
    DEFAULT_VOICE_PROVIDER,
    SUPPORTED_VOICE_PROVIDERS,
    DEFAULT_TR_ENABLED,
    DEFAULT_SAFETY_CHECKS,
    VOICE_MEDIA_RATE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_WAIT_SECONDS,
    DEFAULT_EXPONENTIAL_BACKOFF,
    DEFAULT_BACKOFF_MULTIPLIER,
    DEFAULT_ENABLE_HYDRATION,
)
from .logging_config import setup_logging
from .validation import (
    TemperatureParameters,
    PathParameters,
    BatchParameters,
    ConversationParameters,
    DateParameters,
)

__all__ = [
    # Logging
    "setup_logging",
    # Constants (from constants.py)
    "DEFAULT_TEMPERATURE",
    "MIN_TEMPERATURE",
    "MAX_TEMPERATURE",
    "DEFAULT_LOG_LEVEL",
    "DEFAULT_MCP_LOG_LEVEL",
    "LOG_LEVELS",
    "DEFAULT_COUNT",
    "DEFAULT_CHUNK_SIZE",
    "DEFAULT_METRICS",
    "DEFAULT_VERBOSE",
    "DEFAULT_EVAL_ONLY",
    "DEFAULT_OUTPUT_DIR",
    "DEFAULT_SAMPLED_CONVOS_DIR",
    "DEFAULT_RESULTS_DIR",
    "DATE_FORMAT",
    "TIMESTAMP_FORMAT",
    "DATETIME_FORMAT",
    "ERROR_MESSAGES",
    "SUCCESS_MESSAGES",
    # Voice-specific constants
    "DEFAULT_VOICE_PROVIDER",
    "SUPPORTED_VOICE_PROVIDERS",
    "DEFAULT_TR_ENABLED",
    "DEFAULT_SAFETY_CHECKS",
    "VOICE_MEDIA_RATE",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_WAIT_SECONDS",
    "DEFAULT_EXPONENTIAL_BACKOFF",
    "DEFAULT_BACKOFF_MULTIPLIER",
    "DEFAULT_ENABLE_HYDRATION",
    # Validation (General Pydantic models)
    "TemperatureParameters",
    "PathParameters",
    "BatchParameters",
    "ConversationParameters",
    "DateParameters",
]
