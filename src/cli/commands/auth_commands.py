from ..utils.input_handler import get_user_input
from .auth_prompts import *

def login_user() -> None:
    """Logs a user into the banking app if they are registered."""
    pass

def register_user() -> None:
    """Registers a new user"""
    name = get_user_input(GET_NAME_PROMPT)
    email = get_user_input(GET_EMAIL_PROMPT)
    password = get_user_input(GET_PASSWORD_PROMPT)

    print("Details: ", name, email, password)


