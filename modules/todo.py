#--------handle------------
def handle(user_input,user_data):
    if "add task" in user_input or "new task" in user_input:
        add_task(user_data)
    
    if "view tasks" in user_input or "list task" in user_input or "show tasks" in user_input:
        print_tasks(user_data)
    
    if "task" and "done" in user_input or "task" and "completed" in user_input:
        task_completed(user_data)
    
    elif "delete task" in user_input or "remove task" in user_input:
        remove_task(user_data)

#--------add-tasks----------
def add_task(user_data):
    print("what task do you want to add")
    task = input(":- ")
    user_data["tasks"][task] = False

#---------print-tasks--------
def print_tasks(user_data):
    if not user_data["tasks"]:
        print(" Your to-do list is empty!")
        return

    flag = True
    while flag:
        print("which tasks do you want me to show (all/completed/incompleted)")
        choice = input(":- ").lower().strip()
        
        if choice in ["all", "completed", "incompleted"]:
            flag = False  # Valid input, break the loop
            print("\n Your Tasks:")
            print("-" * 30)
            
            for task_name in user_data["tasks"]:
                status = user_data["tasks"][task_name]
                
                if choice == "all":
                    print(f"[{'🟢' if status else ' '}] {task_name}")
                elif choice == "completed" and status == True:
                    print(f"[🟢] {task_name}")
                elif choice == "incompleted" and status == False:
                    print(f"[🔴] {task_name}")
            print("-" * 30)
        else:
            print("❌ Invalid choice. Please type all, completed, or incompleted.")

#----------task-completed-----
def task_completed(user_data):
    if not user_data["tasks"]:
        print(" No tasks available to mark complete.")
        return

    print("\n Your Tasks:")
    print("-" * 30)
    for task_name in user_data["tasks"]:
        status = user_data["tasks"][task_name]
        print(f"[{'🟢' if status else '🔴'}] {task_name}")
        
    print("Which task did you complete?")
    task = input(":- ").strip()
    
    if task in user_data["tasks"]:
        user_data["tasks"][task] = True
        print(f" Marked '{task}' as completed!")
    else:
        print("❌ Task not found in your list.")

#-----------removing-tasks----
def remove_task(user_data):
    if not user_data["tasks"]:
        print(" No tasks available to remove.")
        return

    print("Which task do you want to completely remove?")
    task = input(":- ").strip()
    
    if task in user_data["tasks"]:
        del user_data["tasks"][task]  # Deletes the key-value pair completely
        print(f" Successfully deleted '{task}' from your list!")
    else:
        print("❌ Task not found in your list.")