from ..utils.input_handler import get_user_input
from src.models import User
from src.services import AuthService
from .auth_prompts import *

auth = AuthService()

def login_user() -> None:
    """Logs a user into the banking app if they are registered."""
    email = get_user_input(GET_EMAIL_PROMPT)
    password = get_user_input(ENTER_PASSWORD_PROMPT)
    # Check if the user details exist using the auth service
    if auth.authenticate_user(email, password):
        print("User has been logged in!")
        return
    print("Login failed")
    return


def register_user() -> None:
    """Registers a new user"""
    name = get_user_input(GET_NAME_PROMPT)
    email = get_user_input(GET_EMAIL_PROMPT)
    password = create_user_password()

    # Create the user object
    user = User(
        name=name,
        email=email,
        password=password
    ).to_dict()

    is_registered, response = auth.register_user(user)

    if is_registered:
        # Change to display formatter later
        print(response)
        return
    print(response)
    return

def create_user_password() -> str:
    while True:
        password = get_user_input(GET_PASSWORD_PROMPT)
        # Confirm the user's password
        confirm_password = get_user_input(CONFIRM_PASSWORD_PROMPT)
        if password == confirm_password:
            break
        print("Passwords do not match! Please try again...")
    return password
