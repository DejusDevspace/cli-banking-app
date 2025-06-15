from ..database import DatabaseManager

class AuthService:
    def __init__(self):
        self.current_user = None
        self.db = DatabaseManager()
        # Initialize the database when service starts
        self.db.data = self.db.load_data()

    def authenticate_user(self, user_id: str, password: str):
        self.current_user = "Load user data and return..."

    def register_user(self, user_data: dict) -> tuple[bool, str]:
        """Register a new user"""
        # Ensure database is loaded
        if not self.db.data:
            self.db.data = self.db.load_data()

        # Validate required fields
        required_fields = ["name", "password", "email"]
        for field in required_fields:
            if field not in user_data:
                return False, f"Missing required field: {field}"

        # Check if username or email already exists
        users = self.db.data.get("users", {})
        for existing_user in users.values():
            if existing_user.get("name") == user_data["name"]:
                return False, "Username already exists! Login instead"
            if existing_user.get("email") == user_data["email"]:
                return False, "Email already exists! Login instead"


        user_id = user_data["id"]
        # Add user to the database structure
        self.db.data["users"][user_id] = user_data

        # Save the updated database
        if self.db.save_data():
            return True, f"Success! User ID: {user_id}"
        else:
            # Remove user from memory if save failed
            del self.db.data["users"][user_id]
            return False, "Failed to save user to database"
