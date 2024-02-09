import json

def login():
    print("\nPlease enter your login info:")
    email = input("Email: ")
    password = input("Password: ")
    try:
        file = open('users.json', 'r')
        users_data = json.load(file)
        file.close()
    except:
        users_data = []
    
    for user in users_data:
        if user["email"] == email and user["password"] == password:
            print("\033[92m\nLogin successful!\033[0m")
            return email
    print("\033[91m\nInvalid email or password.\033[0m")
    return None