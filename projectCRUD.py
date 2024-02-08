import json
import datetime

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def create_project(projects, user_email):
    print("Please enter project details:")
    title = input("Title: ")
    details = input("Details: ")
    total_target = float(input("Total target (Ex. 10000 EGP): "))
    start_time = input("Start time (YYYY-MM-DD): ")
    if not validate_date(start_time):
        print("Invalid date format.")
        return
    end_time = input("End time (YYYY-MM-DD): ")
    if not validate_date(end_time):
        print("Invalid date format.")
        return
    projects[title] = {'title': title,
                       'details': details,
                       'total_target': total_target,
                       'start_time': start_time,
                       'end_time': end_time,
                       'owner': user_email}
    with open('projects.json', 'w') as f:
        json.dump(projects, f)
    print("Project created successfully!")

def view_projects(projects):
    print("All Projects:")
    for project in projects.values():
        print(project)

def edit_project(projects, user_email):
    print("Please select a project to edit:")
    for i, project in enumerate(projects.values()):
        print(f"{i + 1}. {project['title']}")
    choice = int(input("Enter the number corresponding to the project you want to edit: "))
    project_titles = list(projects.keys())
    selected_project_title = project_titles[choice - 1]
    if projects[selected_project_title]['owner'] == user_email:
        print("Edit project:")
        # not implemented yet
    else:
        print("You are not the owner of this project. Access denied.")

def delete_project(projects, user_email):
    print("Please select a project to delete:")
    for i, project in enumerate(projects.values()):
        print(f"{i + 1}. {project['title']}")
    choice = int(input("Enter the number corresponding to the project you want to delete: "))
    project_titles = list(projects.keys())
    selected_project_title = project_titles[choice - 1]
    if projects[selected_project_title]['owner'] == user_email:
        del projects[selected_project_title]
        with open('projects.json', 'w') as f:
            json.dump(projects, f)
        print("Project deleted successfully!")
    else:
        print("You are not the owner of this project. Access denied.")
