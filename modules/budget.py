import os 
import json

"""

#required outcomes
1. add income
2. add expenses
3. view total expenses
4. viewbalance (income + savings - expenses)
5. view expense by catagory
6. reset expenses
7. quit

"""


def clear():
    os.system("cls" if os.name== "nt" else "clear")

def handle(user_input,user_data):
    file_name = budget_login(user_data)
    file = open_json_file(file_name)
    if any(word in user_input for word in ["add income",'supplement income',"augment earnings","boost revenue"]):
        add_income(file)

    elif any(word in user_input for word in ["add expense","incur costs","increase spending","accumulate charges"]):
        add_expense(file)

    elif any(word in user_input for word in ["view total expenses","view expenses","show total costs","check spending"]):
        view_total_balance(file)

    elif any(word in user_input for word in ["view balance", "check balance", "show budget", "remaining funds"]):
        view_total_balance(file)

    elif any(word in user_input for word in ["reset expenses", "clear expenses", "wipe records", "start fresh"]):
        reset_all_expenses(file)

    elif any(word in user_input for word in ["quit", "exit", "stop", "close"]):
        return quit_budget(file)

    else:
        print("Command not recognized. Please try phrasing it differently.")
    
def open_json_file(file_name):
    #print(dir(json))
    try:
        with open(file_name,"r") as file:
            data = json.load(file)
            return data
    except:
        current_dir = os.getcwd()
        template_path = os.path.join(current_dir,"assets","json_template.json")
        with open(template_path,"r") as file:
            template_contents = json.load(file) 
        template_contents["file_name"] = file_name
        with open(file_name, "w") as file:
            json.dump(template_contents,file,indent=4)
        return template_contents

def save_json_file(file):
    file_name = file["file_name"]
    with open(file_name, "w") as f:
            json.dump(file,f,indent=4)

def budget_login(user_data):
    user_id = user_data["user_id"]
    file_name_part2 = user_id + ".json"
    current_dir = os.getcwd()
    file_name = os.path.join(current_dir,"data","budget_jsons",file_name_part2)
    os.makedirs(os.path.join(current_dir,"data","budget_jsons"),exist_ok=True)
    return file_name

def add_income_function(user_income,file):
    file["current"]["income"] = user_income
    save_json_file(file)

def add_income(file):
    runing = True
    while runing:
        print("please enter the income you want to add")
        income = input(":- ")
        try:
            income = float(income)
            if income >= 0:
                add_income_function(income,file)
                runing = False
            else:
                print("please enter a positive value")
        except:
            print("please enter a number")

def add_expense_function(catagory,value,file):
    if catagory in file["current"]["expenses"]:
        file["current"]["expenses"][catagory] += value
    else:
        file["current"]["expenses"][catagory] = value
    save_json_file(file)

def add_expense(file):
    print("please enter the catogory you want to add expense to ")

    expense_list = list(file["current"]["expenses"].keys())
    count = 1
    for expense_name in expense_list:
        print(f"{count}:- {expense_name}")
        count += 1
    print(f"{count}:- just type the name and it will be added")
    user_catagory_input = input()

    if user_catagory_input.isdigit():
        index = int(user_catagory_input) - 1
        if 0 <= index < len(expense_list):
            user_catagory_input = expense_list[index]

    clear()
    print(f"how much amount do you want to add to {user_catagory_input}")
    running = True
    while running:
        user_value_input = input()
        try:
            user_value_input = float(user_value_input)
            add_expense_function(user_catagory_input,user_value_input,file)

            total_expenses = sum(file["current"]["expenses"].values())
            balance = file["current"]["income"] + file["savings"] - total_expenses
            if balance < 0:
                print(f"⚠️ Warning: you are now {abs(balance)} over budget!")
            running = False
        except:
            print("please enter a number :-")

def view_total_expenses(file):
    count,total=1,0
    for catagory,value in file["current"]["expenses"].items():
        print(f"{count}:- {catagory} = {value}")
        count+=1
        total+=value
    print(f"this brings your total expense amount to be :- {total}")

def view_total_balance(file):
    total_expenses = sum(file["current"]["expenses"].values())
    total_balance = file["current"]["income"] + file["savings"]
    current_balance = total_balance - total_expenses
    print(f"your current balance is {current_balance} \n as we subtract total expense of {total_expenses} \n from the initial balance {total_balance}")

def remove_expense(file):
    print("which expense do you want to remove")
    clock = 1
    file_expense_list = list(file["current"]["expenses"]) 
    for expense in file_expense_list:
        print(f"{clock}:- {expense}")
        clock+=1
    user_input = input()
    if user_input.isdigit():
        user_input = int(user_input)
        index = user_input-1
        try:
            del file["current"]["expenses"][file_expense_list[index]]
            save_json_file(file)
        except IndexError:
            print("Index exides the lenght of the expenses")
    else:
        try:
            del file["current"]["expenses"][user_input]
            save_json_file(file)
        except KeyError:
            print("the name you provided does not exist as an expense")

def quit_budget(file):
    print("exiting budget module...")
    save_json_file(file)
    return "quit"
    
def reset_all_expenses(file):
    print("reseting all expenses")
    file["current"]["expenses"] = {}
    save_json_file(file)

def end_setion(file):
    print("ending setion")
    sub_dist_history = file["current"]
    if len(file["history"])<5:
        file["history"].append(sub_dist_history)
        save_json_file(file)
    else:
        file["history"].pop(0)
        file["history"].append(sub_dist_history)
        save_json_file(file)


if __name__ == "__main__":
    file_name = budget_login({'user_id': '1', 'password': '1234', 'username': 'admin', 'is_locked': True, 'budget': [], 'tasks': {'make tea': True}, 'contacts': {'samar': []}, 'grades': [{'physics': [50.0, 40.0], 'chemistry': [60.0, 30.0], 'math': [70.0, 40.0]}], 'journal': {'2026-07-26 21:37:57.076920': 'data\\journals\\journal_admin_260726_213757.txt'}})
    print(file_name)
    file = open_json_file(file_name)
    #add_income(file)
    #add_expense(file)
    view_total_balance(file)
    view_total_expenses(file)
    #add_expense_function("food",15,file)
    #add_income_function(200,file)
    #save_json_file(file_name,{"salary":201})