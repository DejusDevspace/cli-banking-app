"""
Main file for the banking cli app
"""
from cli import input_handler
from cli.commands import login_user, register_user
from prompts import *


def main():
    print("########## WELCOME TO THE BANKING APP ##########")
    option = input_handler.get_user_input(WELCOME_PROMPT)
    if option == "1":
        login_user()
    if option == "2":
        register_user()




if __name__ == "__main__":
    main()
