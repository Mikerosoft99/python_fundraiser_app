import json
import datetime

def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def create_project(projects, user_email):
    print("\nPlease enter project details:")
    title = input("Title: ").title()
    details = input("Details: ").capitalize()
    while True:
        try:
            total_target = float(input("Total target (i.e. 10000 EGP): "))
            break
        except ValueError:
            print("\033[91m\nInvalid input. Please enter a valid number.\033[0m\n")

    while True:
        start_time = input("Start time (YYYY-MM-DD): ")
        if not validate_date(start_time):
            print("\033[91m\nInvalid date format.\033[0m")
        else:
            break
    
    while True:
        end_time = input("End time (YYYY-MM-DD): ")
        if not validate_date(end_time):
            print("\033[91m\nInvalid date format.\033[0m")
        elif start_time >= end_time:
            print("\033[91m\nEnd time must be after start time.\033[0m")
        else:
            break

    new_project = {'title': title,
                'details': details,
                'total_target': total_target,
                'start_time': start_time,
                'end_time': end_time,
                'owner': user_email}

    projects.append(new_project)

    file = open('projects.json', 'w')
    json.dump(projects, file, indent=1)
    file.close()
    print("\033[92m\nProject created successfully!\033[0m")

def view_projects(projects):
    print("\nAll Projects:")
    print("-"*30)
    for project in projects:
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Total Target: {project['total_target']} EGP")
        print(f"Start Time: {project['start_time']}")
        print(f"End Time: {project['end_time']}")
        print(f"Owned by: {project['owner']}")
        print("-"*30)

def edit_project(projects, user_email):
    print("\nPlease select a project to edit:")

    for i, project in enumerate(projects):
        print(f"{i + 1}. {project['title']}")

    try:
        choice = int(input("Enter the number of the project you want to edit: "))
    except ValueError:
        print("\033[91m\nInvalid input. Please enter a valid number.\033[0m")
        return

    choice -= 1

    if choice < 0 or choice >= len(projects):
        print("\033[91m\nInvalid project number.\033[0m")
        return

    selected_project = projects[choice]
    
    if selected_project['owner'] != user_email:
        print("\033[91m\nYou are not the owner of this project. Access denied.\033[0m")
        return

    print("Edit project:")
    selected_project['title'] = input(f"New title ({selected_project['title']}): ")
    selected_project['details'] = input(f"New details ({selected_project['details']}): ")
    try:
        new_total_target = float(input(f"New total target ({selected_project['total_target']} EGP): "))
    except ValueError:
        print("\033[91m\nInvalid input. Please enter a valid number.\033[0m")
        return

    selected_project['total_target'] = new_total_target

    start_time = input(f"New start time ({selected_project['start_time']}): ")
    if not validate_date(start_time):
        print("\033[91mInvalid date format.\033[0m")
        return
    selected_project['start_time'] = start_time

    end_time = input(f"New end time ({selected_project['end_time']}): ")
    if not validate_date(end_time):
        print("\033[91mInvalid date format.\033[0m")
        return
    selected_project['end_time'] = end_time

    file = open('projects.json', 'w')
    json.dump(projects, file, indent=1)
    file.close()

    print("\033[92m\nProject edited successfully!\033[0m")

def delete_project(projects, user_email):
    print("Please select a project to delete:")
    for i, project in enumerate(projects):
        print(f"{i + 1}. {project['title']}")

    try:
        choice = int(input("Enter the number of the project you want to delete: "))
    except ValueError:
        print("\033[91m\nInvalid input. Please enter a valid number.\033[0m")
        return

    choice -= 1

    if choice < 0 or choice >= len(projects):
        print("\033[91m\nInvalid project number.\033[0m")
        return

    selected_project = projects[choice]

    if selected_project['owner'] == user_email:
        confirmation = input(f"Are you sure you want to delete '{selected_project['title']}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            del projects[choice]
            file = open('projects.json', 'w')
            json.dump(projects, file, indent=1)
            file.close()
            print("\033[92mProject deleted successfully!\033[0m")
        else:
            print("\033[91mDeletion canceled.\033[0m")
    else:
        print("\033[91m\nYou are not the owner of this project. Access denied.\033[0m")