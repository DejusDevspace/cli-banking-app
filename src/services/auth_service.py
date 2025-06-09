from ..database import DatabaseManager

class AuthService:
    def __init__(self):
        self.current_user = None

    def authenticate_user(self, user_id, password):
        self.current_user = ""
