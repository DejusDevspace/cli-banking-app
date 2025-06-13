from ..database import DatabaseManager

class AuthService:
    def __init__(self):
        self.current_user = None

    def authenticate_user(self, user_id: str, password: str):
        self.current_user = "Load user data and return..."

    def register_user(self, user: dict):
        pass
