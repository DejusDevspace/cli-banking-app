def get_user_input(prompt, input_type="string") -> str:
    """Get and validate user input"""
    prompt = "{}\n⇛ ".format(prompt)
    response = input(prompt)
    if not response:
        raise ValueError("Input field must not be empty!")
    return response
