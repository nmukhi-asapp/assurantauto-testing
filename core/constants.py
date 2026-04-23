"""
Centralized constants for the repository.

This module consolidates all constants that were duplicated across multiple files,
providing a single source of truth for configuration values.
"""

# Temperature settings for LLM operations
DEFAULT_TEMPERATURE = 0.0
MIN_TEMPERATURE = 0.0
MAX_TEMPERATURE = 2.0

# Logging configuration
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_MCP_LOG_LEVEL = (
    "ERROR"  # Less verbose for MCP tools to avoid JSON-RPC interference
)
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

# Scenario execution defaults
DEFAULT_COUNT = 1
DEFAULT_CHUNK_SIZE = None
DEFAULT_METRICS = False
DEFAULT_VERBOSE = False
DEFAULT_EVAL_ONLY = False

# File and directory defaults
DEFAULT_OUTPUT_DIR = "output"
DEFAULT_SAMPLED_CONVOS_DIR = "sampled_convos"
DEFAULT_RESULTS_DIR = "results"

# Date format constants
DATE_FORMAT = "%Y-%m-%d"
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# AWS and service configuration
DEFAULT_TEAM = "research"
DEFAULT_AWS_PROFILE = "dev-sso-gen-agent-ro"

# Cost tracking constants
COST_TRACKING_PURPOSE = "llmbot"
COST_TRACKING_NAME = "generative-agent-scenario-tests"
COST_TRACKING_OWNER = "team-genagent-core"

# Unleash configuration
UNLEASH_APP_NAME = "generative-agent"

# File extensions
EXCEL_EXTENSION = ".xlsx"
JSON_EXTENSION = ".json"
YAML_EXTENSION = ".yaml"
CSV_EXTENSION = ".csv"

# Excel formatting constants
MAX_DISPLAY_ITEMS = 5
MAX_DESCRIPTION_LENGTH = 100
MAX_SETTINGS_VALUE_LENGTH = 200
TRUNCATE_SUFFIX = "..."

# Validation constants
MIN_PAGINATION_OFFSET = 0
MIN_PAGINATION_COUNT = 1
MAX_PAGINATION_COUNT = 1000
MIN_CONVERSATIONS = 1
MAX_CONVERSATIONS = 10000

# GACS environment constants
GACS_ENVIRONMENTS = ["prod", "sandbox"]
GACS_DEFAULT_ENVIRONMENT = "prod"

# Evaluation result constants
EVALUATION_PASSED = "PASSED"
EVALUATION_FAILED = "FAILED"
EVALUATION_RESULTS = [EVALUATION_PASSED, EVALUATION_FAILED]


# Common error messages
ERROR_MESSAGES = {
    "FILE_NOT_FOUND": "File not found: {path}",
    "DIRECTORY_NOT_FOUND": "Directory not found: {path}",
    "INVALID_PARAMETER": "Invalid parameter {name}: {value}",
    "VALIDATION_FAILED": "Validation failed: {reason}",
    "SERVICE_ERROR": "Service error occurred: {error}",
    "CONFIGURATION_ERROR": "Configuration error: {error}",
    "PROCESSING_ERROR": "Processing failed: {error}",
}

# Success messages
SUCCESS_MESSAGES = {
    "FILE_CREATED": "Successfully created file: {path}",
    "PROCESSING_COMPLETE": "Processing completed successfully",
    "VALIDATION_PASSED": "Validation passed",
    "SERVICE_READY": "Service is ready",
    "OPERATION_SUCCESS": "Operation completed successfully",
}

# Time-related constants
DEFAULT_DAYS_BACK = 7
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

# Data processing constants
DEFAULT_BATCH_SIZE = 15
MAX_BATCH_SIZE = 100
MIN_BATCH_SIZE = 1

# Environment variable names
ENV_VARS = {
    "OPENAI_API_KEY": "OPENAI_API_KEY",
    "GACS_ASSISTANT_ID": "GACS_ASSISTANT_ID",
    "LOG_LEVEL": "LOG_LEVEL",
    "SERVER_HOST": "SERVER_HOST",
    "SERVER_PORT": "SERVER_PORT",
    "RELOAD": "RELOAD",
    "AWS_PROFILE": "AWS_PROFILE",
    "GACS_BRANCH": "GACS_BRANCH",
    "GACS_HOST": "GACS_HOST",
}

# ============================================================================
# Voice-Specific Constants (Added for V2 Voice Support)
# ============================================================================

# Voice channel configuration
DEFAULT_VOICE_PROVIDER = "vapi"
SUPPORTED_VOICE_PROVIDERS = ["vapi", "openai"]
DEFAULT_TR_ENABLED = (
    True  # Talker-Reasoner mode (full Voice Assistant + Digital GenAgent capabilities)
)
DEFAULT_SAFETY_CHECKS = False  # VAPI (default provider) doesn't support safety checks
VOICE_MEDIA_RATE = 8000  # Audio sample rate for voice

# Retry configuration for resilience
DEFAULT_MAX_RETRIES = 3
DEFAULT_WAIT_SECONDS = 2.0
DEFAULT_EXPONENTIAL_BACKOFF = False
DEFAULT_BACKOFF_MULTIPLIER = 2.0

# Conversation hydration
DEFAULT_ENABLE_HYDRATION = True
