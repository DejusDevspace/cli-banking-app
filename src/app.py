"""
Main file for the banking cli app
"""
from src.cli import input_handler
from src.cli.commands import login_user, register_user
from src.prompts import *


def main():
    print("########## WELCOME TO THE BANKING APP ##########")
    option = input_handler.get_user_input(WELCOME_PROMPT)
    if option == "1":
        print("########## PLEASE ENTER YOUR LOGIN DETAILS ##########")
        login_user()
    elif option == "2":
        print("######### FILL ALL THE DETAILS BELOW TO CREATE YOUR ACCOUNT ##########")
        register_user()
    else:
        print("Invalid option selected. Please try again!")

if __name__ == "__main__":
    main()
