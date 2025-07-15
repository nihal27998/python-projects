def show_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\n📋 Your To-Do List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\n✅ Your To-Do List is empty!")
    except FileNotFoundError:
        print("\nNo tasks found. Let's start a new list!")

def add_task():
    task = input("Enter the new task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to delete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_num <= len(tasks):
            del tasks[task_num - 1]
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n🛠️ To-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! 🖐️")
            break
        else:
            print("Invalid option. Try again.")

main()
 