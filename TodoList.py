FILE_NAME = "TodoList.txt"

def add_to_list(task):
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

def delete_task(task_to_delete):
    existing_tasks = []
    # Read existing tasks from the file into a list
    with open(FILE_NAME, 'r') as file:
        existing_tasks = file.readlines()
    task_to_delete += "\n"
    # Remove the task you want to delete from the list
    if task_to_delete in existing_tasks:
        existing_tasks.remove(task_to_delete)

    # Open the file in read-write mode and truncate it to empty its content
    with open(FILE_NAME, 'r+') as file:
        file.truncate()

    # Write the updated list back to the file
    with open(FILE_NAME, 'a') as file:
        file.writelines(existing_tasks)

def edit_task(task_to_edit, new_task):
    existing_tasks = []
    # Read existing tasks from the file into a list
    with open(FILE_NAME, 'r') as file:
        existing_tasks = file.readlines()
    
    task_to_edit += "\n"
    new_task += "\n"

    # Locate and modify the task you want to edit in the list
    if task_to_edit in existing_tasks:
        existing_tasks.remove(task_to_edit)

    existing_tasks.append(new_task)

    # Open the file in read-write mode and truncate it to empty its content
    with open(FILE_NAME, 'r+') as file:
        file.truncate() 

    # Write the updated list back to the file
    with open(FILE_NAME, 'a') as file:
        file.writelines(existing_tasks)

def display_list():
    print()
    with open(FILE_NAME, "r") as file:
        for line in file:
            print(line.strip())
    print()

def main():
    options = ["add", "edit", "delete"]
    display_list()
    while True:
        while True:
            option = input("Would you like to add, edit or delete tasks? ")
            if option not in options:
                print("Invalid option. Try again.")
            else:
                break
        if option == "add":
            task = input("Please add your task here: ")
            add_to_list(task)
            display_list()
        elif option == "delete":
            task = input("Please enter the task to delete: ")
            delete_task(task)
            display_list()
        else:
            task_to_edit = input("Please enter the task to edit: ")
            new_task = input("Please enter the new task: ")
            edit_task(task_to_edit, new_task)
            display_list()
        choice = input("Would you like to continue? (Y/N)")
        if choice == "N":
            break


main()