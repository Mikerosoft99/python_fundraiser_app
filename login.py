import json

def login(users):
    print("Please enter your login credentials:")
    email = input("Email: ")
    password = input("Password: ")
    try:
        file = open('users.json', 'r')
        users_data = json.load(file)
        file.close()
    except FileNotFoundError:
        users_data = []
    if email in users_data and users_data[email]['password'] == password:
        print("Login successful!")
        return email
    else:
        print("Invalid email or password.")
        return None