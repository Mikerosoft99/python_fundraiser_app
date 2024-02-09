import json

def login():
    print("\nPlease enter your login credentials:")
    email = input("Email: ")
    password = input("Password: ")
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = []
    
    for user in users_data:
        if user["email"] == email and user["password"] == password:
            print("\033[92m\nLogin successful!\033[0m")
            return email
    print("\033[91m\nInvalid email or password.\033[0m")
    return None