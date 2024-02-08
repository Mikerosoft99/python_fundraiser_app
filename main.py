import json
import login
import register
import projectCRUD


def get_users():
    try:
        file = open('users.json', 'r')
        file.close()
        return json.load(file)
    except:
        return []

def get_projects():
    try:
        file = open('projects.json', 'r')
        file.close()
        return json.load(file)
    except:
        return []
    
def main():
    users = get_users
    projects = get_projects
    
    while True:
        print("\nWelcome to Fundraise App!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register.register(users)
        elif choice == '2':
            user_email = login.login(users)
            if user_email:
                while True:
                    print("\n1. Create Project")
                    print("2. View Projects")
                    print("3. Edit Project")
                    print("4. Delete Project")
                    print("5. Logout")
                    inner_choice = input("Enter your choice: ")
                    if inner_choice == '1':
                        projectCRUD.create_project(projects, user_email)
                    elif inner_choice == '2':
                        projectCRUD.view_projects(projects)
                    elif inner_choice == '3':
                        projectCRUD.edit_project(projects, user_email)
                    elif inner_choice == '4':
                        projectCRUD.delete_project(projects, user_email)
                    elif inner_choice == '5':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
