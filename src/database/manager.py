import json
from typing import Dict, List
import os
from datetime import datetime


class DatabaseManager:
    def __init__(self, database_path="./data/database.json"):
        self.database_path = database_path
        self.data = None

    def _initialize_database(self) -> Dict:
        """Initialize database structure if file does not exist"""
        default_structure = {
            "users": {},
            "accounts": {},
            "transactions": {},
        }

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.database_path), exist_ok=True)

        # Create file with default structure if it doesn't exist
        if not os.path.exists(self.database_path):
            self._write_to_file(default_structure)
            return default_structure

        # Load existing data
        return self.load_data()

    def load_data(self) -> Dict:
        """Load data from JSON file"""
        try:
            with open(self.database_path, "r") as f:
                self.data = json.load(f)
            return self.data
        except FileNotFoundError:
            print(f"Database file not found: {self.database_path}")
            return self._initialize_database()
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return {}
        except Exception as e:
            print(f"Error loading data from database: {e}")
            return {}

    def _write_to_file(self, data: Dict) -> bool:
        """Write data to JSON file with proper formatting"""
        try:
            with open(self.database_path, "w") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error writing to database: {e}")
            return False

    def save_data(self) -> bool:
        """Save current data to file"""
        return self._write_to_file(self.data)
