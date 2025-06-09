import uuid
from typing import Dict
from datetime import datetime


class User:
    def __init__(self, name: str, email: str, password: str, user_id: str = None):
        self.id = user_id if user_id else str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.created_at = datetime.now().isoformat()
        self.accounts = []  # List of account IDs belonging to this user

    def to_dict(self) -> Dict:
        """Convert User object to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "accounts": self.accounts
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create User object from dictionary"""
        user = cls(data["name"], data["email"], data["password"], data["id"])
        user.created_at = data.get("created_at", datetime.now().isoformat())
        user.accounts = data.get("accounts", [])
        return user
