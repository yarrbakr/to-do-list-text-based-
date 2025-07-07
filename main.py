from typing import Any, Dict, Tuple
import os

#clearing screen 
def clear_screen():
    if os.name == "nt":
        _= os.system("cls")
    else:
        _=os.system("clear")

#database dictionary
data_base : dict = {
    "abubakar" : "123",
    "ali" : "456",
}

#tasks dictionary
user_tasks : dict = {
    "abubakar" : [[1, "Get up at 5 am"], [2, "visit grandma"]],
    "ali" : [[1, "Complete project"], [2, "visit mamu"]]
}


#Main menu:
def main_menu():
    check : bool = True
    choice : int
    while check:
        print("===================================================")
        print("WELCOME TO MY TO-DO-LIST PROJECT")
        print("===================================================")
        print("\n1. Login")
        print("\n2. Register")
        choice = int(input("Enter (1/2): "))
        if choice == 1:
            clear_screen()
            login()
            break
        elif choice == 2:
            clear_screen()
            register()
            break
        else:
            print("Enter a valid choice(1/2)")

#register:
def register():
    print("===================================================")
    print("REGISTERATION PAGE")
    print("===================================================") 
    new_user = input("Enter your username:\t")
    new_password = input("Enter your password:\t")
    data_base[new_user] = new_password
    print(data_base)
    clear_screen()
    login()

#login
def login():
    print("===================================================")
    print("LOGIN PAGE")
    print("===================================================")
    sample_user_name : str = input("Enter username:\t")
    sample_user_password : str = input("Enter password:\t")
    for user, password in data_base.items():
        if sample_user_password == password and sample_user_name == user:
            print("access granted")
            tasks_display(sample_user_name)
            break
    else:
        print("access denied")

def tasks_display(sample_user_name):
    tasks = user_tasks.get(sample_user_name, []) #accessing the tasks for the specific user

    if not tasks:
        print(f"{sample_user_name} has no tasks yet.")
        return

    print(f"\n{sample_user_name}'s Tasks:")
    print("-------------------------------")
    for task_id, description in tasks:
        print(f"{task_id}. {description}")
        print("---------------------------")

    #task management option:
    print("\nOptions: ")
    print("1. Add tasks | 2. Delete tasks | 3. Logout")
    choice = input("Choose: ")

    if choice == "1":
        new_task = input("Enter new task: ")
        next_id = len(tasks) + 1
        user_tasks[sample_user_name].append([next_id, new_task])
        tasks_display(sample_user_name)
    elif choice == "2":
        del_id = int(input("Enter task id to delete: "))
        user_tasks[sample_user_name] = [t for t in tasks if t[0] != del_id]
        tasks_display(sample_user_name)
    else:
        main_menu()

#execution
main_menu()
