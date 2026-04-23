"""
Centralized logging configuration for the repository.

This module provides a single point of configuration for all logging needs,
eliminating the duplicated logging.basicConfig() calls throughout the codebase.
"""

import logging
import sys
from typing import Optional


def setup_logging(
    name: str,
    level: str = "INFO",
    format_string: Optional[str] = None,
    configure_root: bool = True,
) -> logging.Logger:
    """
    Set up centralized logging configuration.

    This is the primary logging function for the entire repository,
    replacing all scattered logging.basicConfig() calls with a single,
    consistent configuration approach.

    Args:
        name: Logger name (use descriptive names like "mcp-gacs", "data-processor")
        level: Logging level ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
        format_string: Custom format string (uses default if None)
        configure_root: Whether to configure the root logger (default: True)

    Returns:
        Configured logger instance

    Example:
        >>> logger = setup_logging("mcp-gacs")
        >>> logger.info("GACS server started")

        >>> logger = setup_logging("data-processor", level="DEBUG")
        >>> logger.debug("Processing data batch")
    """
    # Default format string with timestamp, name, level, and message
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Configure root logger only once to avoid duplicate handlers
    if configure_root and not logging.root.handlers:
        logging.basicConfig(
            level=getattr(logging, level.upper(), logging.INFO),
            format=format_string,
            stream=sys.stdout,
        )

    # Create and return named logger
    logger = logging.getLogger(name)

    # Set level for the named logger
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    return logger


# Common logging utilities
def log_function_entry(logger: logging.Logger, func_name: str, **kwargs):
    """
    Log function entry with parameters.

    Args:
        logger: Logger instance
        func_name: Function name
        **kwargs: Function parameters to log
    """
    params = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    logger.debug(f"Entering {func_name}({params})")


def log_function_exit(logger: logging.Logger, func_name: str, result=None):
    """
    Log function exit with optional result.

    Args:
        logger: Logger instance
        func_name: Function name
        result: Optional result to log
    """
    if result is not None:
        logger.debug(f"Exiting {func_name} with result: {type(result).__name__}")
    else:
        logger.debug(f"Exiting {func_name}")


def log_error_with_context(logger: logging.Logger, error: Exception, context: str):
    """
    Log error with additional context information.

    Args:
        logger: Logger instance
        error: Exception that occurred
        context: Additional context information
    """
    logger.error(f"{context}: {type(error).__name__}: {str(error)}", exc_info=True)
