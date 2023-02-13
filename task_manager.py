from datetime import date

# Create a function that converts date to european format.
# Convert date into a string.
# Convert the date back into a list split by '-'.
# Reformat the date to DD-MM-YYY
def eurodate():
    current_date = date.today()
    date_string = str(current_date)
    date_list = date_string.split("-")
    today = (f"{date_list[2]}-{date_list[1]}-{date_list[0]}")
    return today

# Enter the register new user tool as admin.
# Ask the user to enter the new username and password. Password needs to be confirmed.
# If the username is already taken, ask the user to try again.
# If the passwords do not match, ask the user to enter the details again.
# If the input is accepted, write the new username and password to the 'user.txt' file.
def reg_user():
    print("\n---------- Register a new user ----------\n")
    with open("user.txt", "a") as user_file:
        new_user_input = input("Enter a new username: ")
        new_pass_input = input("Enter the new user's password: ")
        new_pass_confirm = input("Confirm the new user's password: ")
        while True:
            if new_user_input in user_list:
                print("\nThis username is already taken.")
                new_user_input = input("\nEnter a new username: ")
                new_pass_input = input("Enter the new user's password: ")
                new_pass_confirm = input("Confirm the new user's password: ")
            elif new_pass_input != new_pass_confirm:
                print("\nThe passwords don't match. Please try again: ")
                new_user_input = input("\nEnter a new username: ")
                new_pass_input = input("Enter the new user's password: ")
                new_pass_confirm = input("Confirm the new user's password: ")
            elif new_pass_input == new_pass_confirm:
                user_file.write(f"\n{new_user_input}, {new_pass_input}")
                print("\nNew user added succesfully.")
                break

# Enter the adding tasks tool.
# Ask the user to enter the required details for the new task.
# Adds in the assigned date automatically.
# Write the task to the 'tasks.txt' file on a new line
def add_task():
    with open("tasks.txt", "a") as tasks_file:
        print("\n---------- Add a new task ----------\n")
        new_task_user = input("Enter the username you would like assign a new task to: ")
        new_task_title = input("Enter the title of the task: ")
        new_task_desc = input("Enter the task description: ")
        new_task_due = input("Enter the date the task is due for completion. Please use the format DD-MM-YYYY: ")
        tasks_file.write(f"\n{new_task_user}, {new_task_title}, {new_task_desc}, {eurodate()}, {new_task_due}, No")
        print("\nNew task added succesfully.")

# Enter the view all tasks tool.
# Splits up each tasks and displays it to the user in a readable manner.
def view_all():
    with open("tasks.txt", "r") as tasks_file:
        print("\n---------- View all tasks ----------\n")
        for task in tasks_file:
            task_split = task.split(", ")
            completion = task_split[5].replace("\n", "")
            print(f"""
            Task:        \t{task_split[1]}
            Assigned to: \t{task_split[0]}
            Date assigned: \t{task_split[3]}
            Due date:   \t{task_split[4]}
            Task complete? \t{completion}
            Task description:
            {task_split[2]}
                """)

# Enter the view my tasks tool.
# Checks if there are any tasks assigned to the logged in user.
# If there are, splits each task up and displays then in a readable manner.
def my_tasks():
    with open("tasks.txt", "r") as tasks_file:
        print("\n---------- View my tasks ----------\n")
        i = 0
        for task in tasks_file:
            i += 1
            task_split = task.split(", ")
            completion = task_split[5].replace("\n", "")
            if task_split[0] == username_input:
                print(f"""
                Task {i}:        \t{task_split[1]}
                Assigned to: \t{task_split[0]}
                Date assigned: \t{task_split[3]}
                Due date:   \t{task_split[4]}
                Task complete? \t{completion}
                Task description:
                {task_split[2]}
                    """)

# Enter the edit tasks menu
# Open the 'tasks.txt' file and split each task.
# Ask the user to enter which task they would like to edit                
def edit_task():
    with open("tasks.txt", "r+") as tasks_file:
        task_lines = tasks_file.readlines()
        position = int(input("\nPlease enter the number of the task you would like to edit. Enter '-1' to return to the main menu: ")) - 1
        split_task = task_lines[position].split(", ")

# If the user enters '-1', return to the main menu
    while True:
        if position == -2:
            while authorize == True:
                admin_menu()
            else:
                user_menu()
        else:
            break

# Check if the task chosen is assigned to the logged in user.
# If not ask them to choose the task again.
    while True:
        if split_task[0] != username_input:
            print('\nThis task is not assigned to you.')
            position = int(input("\nPlease enter the number of the task you would like to edit. Enter '-1' to return to the main menu: ")) - 1
            split_task = task_lines[position].split(", ")
        else:
            break
# Ask the user to choose an option.    
    edit = int(input("""\nPlease choose from the following options:
    1. Mark task as complete.
    2. Edit the task.
    """))
# If the user chooses option 1, mark the task as complete and write the update to the 'tasks.txt'
    if edit == 1 and "No" in split_task[5] and split_task[0] == username_input:
        split_task[5] = "Yes\n"
        string = ", ".join(split_task)
        task_lines[position] = string
        with open("tasks.txt", "w") as tasks_file:
            tasks_file.writelines(task_lines)
        print(f"\nTask {position + 1} is now complete.")
# If the user chooses option 2, ask them to choose another option.
    elif edit == 2 and "No" in split_task[5] and split_task[0] == username_input:
        edit_choice = int(input("""\nPlease choose from the following options:
    1. Assign task to new user.
    2. Amend task due date.
        """))
        # If the user chooses option 2, update the user assigned to the task
        # Write the update to 'tasks.txt'
        if edit_choice == 1:
            new_user = input("User: ")
            split_task[0] = new_user
            string = ", ".join(split_task)
            task_lines[position] = string
            with open("tasks.txt", "w") as tasks_file:
                tasks_file.writelines(task_lines)
            print(f"\nTask {position + 1} has now been assigned to {new_user}.")
        # If the user chooses option 2, update the due date of task
        # Write the update to 'tasks.txt'
        elif edit_choice == 2:
            split_task[4] = input("Enter the new due date: ")
            string = ", ".join(split_task)
            task_lines[position] = string
            with open("tasks.txt", "w") as tasks_file:
                tasks_file.writelines(task_lines)
            print(f"\nTask {position + 1} due date has been changed to {split_task[4]}.")
        # If the user chooses an unsiutable option, ask them to choose again.
        else:
            edit_choice = int(input("""\nPlease choose from the following options:
    1. Assign task to new user
    2. Amend task due date"""))
    # If the task has already been marked as complete, output message
    elif "Yes" in split_task[5]:
        print("\nThis task has already been completed.")
    # If the user chooses a task not assigned to them
    # Display error message and ask them to try again
    elif split_task[0] != username_input:
        print('\nThis task is not assigned to you.')
        edit_choice = int(input("""\nPlease choose from the following options:
    1. Assign task to new user
    2. Amend task due date
        """))
    # If the user chooses an unsuitable option, ask again
    else:
        edit_choice = int(input("""\nPlease choose from the following options:
    1. Assign task to new user
    2. Amend task due date
            """))

# Enter the statistics tool as admin.
# If the overview files have not been generated, generates the files
# Access each file and print the corresponsing information
def stats():
    task_overview()
    user_overview()

    print("\n---------- Statistics ----------\n")
    with open("task_overview.txt", "r") as to:
        task_lines = to.readlines()
        print(task_lines[0])
    
    with open("user_overview.txt", "r") as uo:
        user_lines = uo.readlines()
        print(user_lines[0])

"""def task_finder():
    with open("tasks.txt", "r") as tasks_file:
        task_lines = tasks_file.readlines()
        for position, task in enumerate(task_lines):
            print(f"{position}. {task}")"""

# Display the options menu for admin users
# If the user enters an invalid character, display an error message.
def admin_menu():
    while authorize == True:
        menu = input('''\nSelect one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        s - View statistics
        gr - Generate reports
        e - Exit
        : ''').lower()
        
        if menu == "r":
            reg_user()
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            my_tasks()
            edit_task()
        elif menu == 's':
            stats()
        elif menu == 'gr':
            task_overview()
            user_overview()
            print("\n\'task_overview.txt\' and \'user_overview.txt\' have been generated.")
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        elif menu not in ("r", "a", "va", "vm", "s", "gr", "e"):
            print("\nPlease select a valid option.")
        else:
            break

# Display the options menu for non admin users
# If the user selects an option they are not authorized for, display a message.
# If the user enters an invalid character, display an error message. 
def user_menu():
    while authorize == False:
        menu = input('''\nSelect one of the following Options below:
            a - Adding a task
            va - View all tasks
            vm - View my task
            gr - Generate reports
            e - Exit
            : ''').lower()

        if menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()
        elif menu == 'vm':
            my_tasks()
            edit_task()
        elif menu == 'gr':
            task_overview()
            user_overview()
            print("\n\'task_overview.txt\' and \'user_overview.txt\' have been generated.")
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        elif menu not in ("r", "a", "va", "vm", "s", "gr", "e"):
            print("\nPlease select a valid option.")
        elif menu == "r" or menu == "s":
            print("\nYou do not have admin access.")
        else:
            break

# Enter the task overview tool.
# Open 'tasks.txt' and split the tasks.
# Calculate the total amount of tasks.
def task_overview():
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
        total_tasks = (len(tasks))
        completed = 0
        incomplete = 0
        overdue = 0
        
# Calculate the amount of complete and incomplete tasks.
        for i in tasks:
            if 'Yes' in i:
                completed += 1
            else:
                incomplete += 1

# Calculate the percentage of incomplete tasks.
        incomplete_perc = (incomplete / total_tasks) * 100
        
# Open the 'tasks.txt' file again.
    with open("tasks.txt", "r") as task_file:
        tasks_read = task_file.read()
        task_line = tasks_read.splitlines()

# Split each item within each task.
# Check if the due date for each task is before the current date.
# If it is, mark the task as overdue.
        for i in task_line:
            task_split = i.split(",")
            due_date = task_split[4].strip()
            current_date = eurodate().split("-")
            due_list = due_date.split("-")
            if due_list[2] < current_date[2] and 'No' in i:
                overdue += 1
            elif due_list[2] == current_date[2] and due_list[1] < current_date[1] and 'No' in i:
                overdue += 1
            elif due_list[2] == current_date[2] and due_list[1] == current_date[1] and due_list[0] < current_date[0] and 'No' in i:
                overdue += 1

# Calculate the overdue task percentage.
        overdue_perc = (overdue / total_tasks) * 100

# Write the stored information to a new file named 'task_overview.txt'
    with open("task_overview.txt", "w") as to:
        to.write(f"""Total number of tasks: {total_tasks}
Completed tasks: {completed}
Incomplete tasks: {incomplete}
Overdue tasks: {overdue}
Percentage of incomplete tasks: {int(incomplete_perc)}%
Percentage of overdue tasks: {int(overdue_perc)}%
""")

# Enter the user overview tool.
# Open 'user.txt' and split the each user.
# Calculate the total amount of users.
def user_overview():
    with open("user.txt", "r") as user_file:
        users = user_file.readlines()
        number_of_users = len(users)

# Open 'tasks.txt'' and split each task.
# Calculate the total amount of tasks.
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
        all_tasks = len(tasks)
        total_tasks = 0
        completed = 0
        incomplete = 0
        overdue = 0

# Calculate the amount of tasks assigned to the logged in user
        for i in tasks:
            if username_input in i:
                total_tasks += 1

# Calculate the amount of complete and incomplete tasks assigned to the logged in user.
        for i in tasks:
            if 'Yes' in i and username_input in i:
                completed += 1
            elif 'No' in i and username_input in i:
                incomplete += 1

# Calculate the percentage of tasks assigned to the logged in user.
# Calculate the percentage of complete tasks assigned to the user.
# Calculate the percentage of incomplete tasks assigned to the user.
        total_perc = (total_tasks / all_tasks) * 100
        complete_perc = (completed / total_tasks) * 100
        incomplete_perc = (incomplete / total_tasks) * 100

# Open the 'tasks.txt' file again and split each task
    with open("tasks.txt", "r") as task_file:
        tasks_read = task_file.read()
        task_line = tasks_read.splitlines()

# Split each item within each task.
# Check if the due date for each task is before the current date.
# If it is, mark the task as overdue.
        for i in task_line:
            task_split = i.split(",")
            due_date = task_split[4].strip()
            current_date = eurodate().split("-")
            due_list = due_date.split("-")
            if due_list[2] < current_date[2] and 'No' in i and username_input in i:
                overdue += 1
            elif due_list[2] == current_date[2] and due_list[1] < current_date[1] and ("No", username_input) in i:
                overdue += 1
            elif due_list[2] == current_date[2] and due_list[1] == current_date[1] and due_list[0] < current_date[0] and ("No", username_input) in i:
                overdue += 1

# Calculate the percentage of overdue tasks assigned to the logged in user.
        overdue_perc = (overdue / total_tasks) * 100

# Write the stored information to a new file named 'user_overview.txt'
    with open("user_overview.txt", "w") as to:
        to.write(f"""Total number of users: {number_of_users}
Total number of tasks assigned to user: {total_tasks}
Percentage of tasks assigned to user: {int(total_perc)}%
Percentage of complete tasks: {int(complete_perc)}%
Percentage of incomplete tasks: {int(incomplete_perc)}%
Percentage of incomplete and overdue tasks: {int(overdue_perc)}%""")

# Output begins
print("---------- Task Manager ----------")
print("\nUser Login")

# Ask the user for their username and password
username_input = input("\nUsername: ")
pass_input = input("Password: ")

authorize = False
user_list = []
pass_list = []
current_date = date.today()
task_amount = []

# Add each username and password to a separate list
with open("user.txt", "r") as user_file:
    for line in user_file:
        user = line.split(',')[0]
        password = line.split(",")[1]
        user_list += user.split()
        pass_list += password.split()

# Check if the username and password entered match the username and password from the text file. 
# If so, continue to the code below.
# Also checks if the user is an admin. If they are provide admin access.
# If the username or password entered are incorrect:
# display the corresponding message and ask user to enter details again.
while True:
    if username_input in user_list and pass_input in pass_list:
        print(f"\nWelcome, {username_input}.")
        if username_input == "admin":
            authorize = True
        break
    elif username_input not in user_list:
        print("\nThe username you entered is not correct, please try again.\n")
        username_input = input("Username: ")
        pass_input = input("Password: ")
    elif username_input in user_list and pass_input not in pass_list:
        print("\nThe password you entered is not correct, please try again.\n")
        username_input = input("Username: ")
        pass_input = input("Password: ")
    elif username_input not in user_list or pass_input not in pass_list:
        print("\nThe username or password you entered is not correct, please try again.\n")
        username_input = input("Username: ")
        pass_input = input("Password: ")

# Display the options menu for non admin users
# If the user selects an option they are not authorized for, display a message.
# If the user enters an invalid character, display an error message.
while authorize == True:
    admin_menu()

# Display the options menu non admin users
# If the user enters an invalid character, display an error message.
while authorize == False:
    user_menu()