"""
Configuration management for Project Chimney Swift.
Centralizes all system settings with validation.
"""
import os
from typing import Optional
from pydantic import BaseSettings, Field, validator
from pathlib import Path
import logging

class ProjectConfig(BaseSettings):
    """Configuration model with validation."""
    
    # Firebase Configuration
    firebase_credentials_path: Path = Field(
        default=Path("./firebase-credentials.json"),
        description="Path to Firebase service account credentials"
    )
    firebase_database_url: Optional[str] = Field(
        default=None,
        description="Firebase Realtime Database URL"
    )
    
    # AI/ML Configuration
    openai_api_key: Optional[str] = Field(
        default=None,
        description="OpenAI API key for AI model access"
    )
    ai_model: str = Field(
        default="gpt-4",
        description="Default AI model to use"
    )
    max_tokens: int = Field(
        default=2000,
        ge=100,
        le=4000,
        description="Maximum tokens for AI responses"
    )
    
    # System Configuration
    log_level: str = Field(
        default="INFO",
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    )
    retry_attempts: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Number of retry attempts for failed operations"