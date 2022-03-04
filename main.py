from controller import *


def add_employee_from_user_input():
    name = input("Enter the name of the employee: ")
    job_class = input("Enter the job class of the employee: ")
    status = add_employee(name, job_class)
    if status == 0:
        print(f'{name} added to database with job_class = {job_class}')
    input('Hit Enter to Continue\n\n')


def add_project_from_user_input():
    name = input("Enter the name of the project: ")
    add_project(name)


def add_job_from_user_input():
    job_class = input("Enter the job class of the employee: ")
    charge_hour = input("Enter the charge hour of the job class: ")
    add_job(job_class, charge_hour)


def assign_employee_to_project_from_user_input():
    employee_num = input("Enter the employee number: ")
    project_num = input("Enter the project number: ")
    assignment_hours = input("How many hours?")
    assign_employee_to_project(employee_num, project_num, assignment_hours)


def remove_employee_from_user_input():
    employee_num = input("Enter the employee number: ")
    remove_employee(employee_num)


def remove_project_from_user_input():
    project_num = input("Enter the project number: ")
    remove_project(project_num)


def remove_employee_from_project_from_user_input():
    employee_num = input("Enter the employee number: ")
    project_num = input("Enter the project number: ")
    remove_employee_from_project(employee_num, project_num)


def list_employees_in_project():
    project_name = input("Enter the project name: ")
    employee_list = get_employee_list_for_project(project_name)
    for employee in employee_list:
        print(employee)


def rename_project():
    while True:
        try:
            current_project_name = input("Enter the project name: ")
            new_project_name = input("Enter the new project name: ")
            update_project_name(current_project_name, new_project_name)
            print(f'Project name updated to {new_project_name}')
            break
        except Exception as e:
            print(f'An error has occurred. {e}')
        if input("Try Again? (y/n) ").lower() == 'y':
            continue
        else:
            break


def display_menu():
    print("1. Add Employee")
    print("2. Add Project")
    print("3. Add Job")
    print("4. Assign Employee to a Project")
    print("5. Remove Employee")
    print("6. Remove Project")
    print("7. Remove Employee from a Project")
    print("8. List Employees in a Project")
    print("9. Rename Project")
    print("0. Quit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee_from_user_input()
        elif choice == "2":
            add_project_from_user_input()
        elif choice == "3":
            add_job_from_user_input()
        elif choice == "4":
            assign_employee_to_project_from_user_input()
        elif choice == "5":
            remove_employee_from_user_input()
        elif choice == "6":
            remove_project_from_user_input()
        elif choice == "7":
            remove_employee_from_project_from_user_input()
        elif choice == "8":
            list_employees_in_project()
        elif choice == '9':
            rename_project()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
