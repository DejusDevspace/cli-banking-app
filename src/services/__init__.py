"""
Service package for handling logic operations related to the application.
Exports all service classes for easy importing.
"""
from .auth_service import AuthService

__all__ = [
    "AuthService"
]
