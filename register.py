import json
import re

email_pattern = r'\S+@\S+\.\S+'
def validate_email(email):
    return re.fullmatch(email_pattern, email)

def validate_phone(phone):
    return re.match(r'^01[0-9]{9}$', phone)

def register(users):
    try:
        file = open('users.json', 'r')
        users = json.load(file)
    except FileNotFoundError:
        users = []    
    print("Please enter your registration info:")
    # Name
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    if not first_name.isalpha() or not last_name.isalpha():
        print("\033[91mPlease enter a valid name.\033[0m")
        return
    # Email
    email = input("Enter your email address: ")
    if not validate_email(email):
        print("\033[91mInvalid email address. Please enter a valid email address.\033[0m")
        return
    for user in users:
        if user['email'] == email:
            print("\033[91mEmail already exists. Please choose a different one.\033[0m")
            return
    # Password
    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        print("\033[91mPasswords don't match.\033[0m")
        return
    # Phone Number
    phone = input("Mobile phone: ")
    if not validate_phone(phone):
        print("\033[91mInvalid phone number format. Please enter a valid Egyptian phone number.\033[0m")
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
    
    print("\033[32mRegistration successful!\033[0m")