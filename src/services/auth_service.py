from ..database import DatabaseManager
from typing import Optional, Dict

class AuthService:
    def __init__(self):
        self.current_user = None
        self.db = DatabaseManager()
        # Initialize the database when service starts
        self.db.data = self.db.load_data()

    def authenticate_user(self, email: str, password: str) -> tuple[bool, str]:
        """Authenticate user with email and password"""
        # Load the data if it is not available
        if not self.db.data:
            print("Loading data...")
            self.db.data = self.db.load_data()

        # Get the user id from the data
        users = self.db.data.get("users", {})
        for user in users.values():
            # Check if there is a match with email and passwords
            if user.get("email") == email:
                if user.get("password") == password:
                    self.current_user = user
                    return True, "User has been logged in!"
                return False, "Invalid password, please try again!"
        return False, "User does not exist! You may create an account instead."

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

    def get_user_by_email(self, email: str) -> Optional[Dict]:
        """Get user data by user email"""
        if not self.db.data:
            self.db.data = self.db.load_data()

        users = self.db.data.get("users", {})
        for user in users.values():
            if user.get("email") == email:
                return user
        return None

    def get_user_by_name(self, name: str) -> Optional[Dict]:
        """Get user data by name"""
        if not self.db.data:
            self.db.data = self.db.load_data()

        users = self.db.data.get("users", {})
        for user in users.values():
            if user.get("name") == name:
                return user
        return None

    def logout(self):
        """Logout current user"""
        self.current_user = None

    def is_authenticated(self) -> bool:
        """Check if a user is currently authenticated"""
        return self.current_user is not None
