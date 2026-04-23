"""
Centralized validation using Pydantic models.

This module provides clean, type-safe validation for general parameters
using Pydantic models. GACS-specific validation models are in the gacs.models module.
"""

from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field, field_validator

from .constants import (
    MIN_CONVERSATIONS,
    MAX_CONVERSATIONS,
    DATE_FORMAT,
    MIN_TEMPERATURE,
    MAX_TEMPERATURE,
    MIN_BATCH_SIZE,
    MAX_BATCH_SIZE,
)


# General validation models for non-GACS functionality
class TemperatureParameters(BaseModel):
    """Temperature validation for LLM operations."""

    temperature: float = Field(
        default=0.0,
        ge=MIN_TEMPERATURE,
        le=MAX_TEMPERATURE,
        description="Temperature for LLM operations",
    )


class PathParameters(BaseModel):
    """Path validation parameters."""

    file_path: str = Field(min_length=1, description="File path")
    must_exist: bool = Field(default=True, description="Whether path must exist")

    @field_validator("file_path")
    @classmethod
    def validate_path(cls, v: str) -> str:
        path = Path(v)
        # Basic path validation - could be enhanced based on needs
        return str(path.resolve())


class BatchParameters(BaseModel):
    """Batch processing parameters."""

    batch_size: int = Field(
        default=MIN_BATCH_SIZE,
        ge=MIN_BATCH_SIZE,
        le=MAX_BATCH_SIZE,
        description="Batch size for processing",
    )


class ConversationParameters(BaseModel):
    """Conversation count validation."""

    count: int = Field(
        ge=MIN_CONVERSATIONS,
        le=MAX_CONVERSATIONS,
        description="Number of conversations",
    )


class DateParameters(BaseModel):
    """Date validation parameters."""

    date_string: str = Field(min_length=1, description="Date string to validate")
    date_format: str = Field(default=DATE_FORMAT, description="Expected date format")

    @field_validator("date_string")
    @classmethod
    def validate_date(cls, v: str, info) -> str:
        """Validate and normalize date string."""
        try:
            # Parse to ensure valid date
            date_format = info.data.get("date_format", DATE_FORMAT)
            datetime.strptime(v, date_format)  # Validate format
            return v  # Return original if valid
        except ValueError:
            raise ValueError(
                f"Date must be in format {info.data.get('date_format', DATE_FORMAT)}"
            )
