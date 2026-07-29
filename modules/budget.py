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
    pass

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
        with open(file_name, "w") as file:
            json.dump(template_contents,file,indent=4)
        return template_contents

def save_json_file(file_name,full_data):
    with open(file_name, "w") as file:
            json.dump(full_data,file)

def budget_login(user_data):
    user_id = user_data["user_id"]
    file_name_part2 = user_id + ".json"
    current_dir = os.getcwd()
    file_name = os.path.join(current_dir,"data","budget_jsons",file_name_part2)
    os.makedirs(os.path.join(current_dir,"data","budget_jsons"),exist_ok=True)
    return file_name

def add_income(user_income,user_data):
    pass

file_name = budget_login({'user_id': '1', 'password': '1234', 'username': 'admin', 'is_locked': True, 'budget': [], 'tasks': {'make tea': True}, 'contacts': {'samar': []}, 'grades': [{'physics': [50.0, 40.0], 'chemistry': [60.0, 30.0], 'math': [70.0, 40.0]}], 'journal': {'2026-07-26 21:37:57.076920': 'data\\journals\\journal_admin_260726_213757.txt'}})
print(file_name)
open_json_file(file_name)
#save_json_file(file_name,{"salary":201})