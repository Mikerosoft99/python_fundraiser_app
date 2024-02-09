import json
from login import login 
from register import register
from projectCRUD import create_project, edit_project, view_projects, delete_project

def get_projects():
    try:
        file = open('projects.json', 'r')
        projects = json.load(file)
        file.close()
        return projects
    except:
        return []

def main():
    projects = get_projects()
    
    while True:
        print("\033[93mWelcome to Fundraise App!\033[0m")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            user_email = login()
            if user_email:
                while True:
                    print("\n1. Create Project")
                    print("2. View Projects")
                    print("3. Edit Project")
                    print("4. Delete Project")
                    print("5. Logout")
                    inner_choice = input("Enter your choice: ")
                    if inner_choice == '1':
                        create_project(projects, user_email)
                    elif inner_choice == '2':
                        view_projects(projects)
                    elif inner_choice == '3':
                        edit_project(projects, user_email)
                    elif inner_choice == '4':
                        delete_project(projects, user_email)
                    elif inner_choice == '5':
                        break
                    else:
                        print("\033[91m\nInvalid choice. Please try again.\033[0m")
        elif choice == '3':
            break
        else:
            print("\033[91m\nInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main()