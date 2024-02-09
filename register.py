import json
import re

email_pattern = r'\S+@\S+\.\S+'
def validate_email(email):
    return re.fullmatch(email_pattern, email)

def validate_phone(phone):
    return re.match(r'^01[0-9]{9}$', phone)

def register():
    try:
        file = open('users.json', 'r')
        users = json.load(file)
        file.close()
    except:
        users = []
    print("Please enter your registration info:")

    # Name
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    if not first_name.isalpha() or not last_name.isalpha():
        print("\033[91m\nPlease enter a valid name.\033[0m")
        return
    
    # Email
    email = input("Enter your email address: ")
    if not validate_email(email):
        print("\033[91m\nInvalid email address. Please enter a valid email address.\033[0m")
        return
    for user in users:
        if user['email'] == email:
            print("\033[91m\nEmail already exists. Please choose a different one.\033[0m")
            return

    # Password
    password = input("Password: ")
    if len(password) < 8:
        print("\033[91m\nPassword must be at least 8 characters long.\033[0m")
        return
    
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        print("\033[91m\nPasswords don't match.\033[0m")
        return

    # Phone Number
    phone = input("Phone Number (Egyptian): ")
    if not validate_phone(phone):
        print("\033[91m\nInvalid phone number. Please enter an Egyptian phone number format.\033[0m")
        return

    user_data = {'first_name': first_name,
                 'last_name': last_name,
                 'email': email,
                 'password': password,
                 'phone': phone}

    users.append(user_data)

    file = open('users.json', 'w')
    json.dump(users, file, indent=1)
    file.close()

    print("\033[32m\nRegistration successful!\033[0m")