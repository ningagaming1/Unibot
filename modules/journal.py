import os
import datetime

#get the file location
storage_dir = os.path.join("data","journals") 


def handle(user_input,user_data):
    #print("runing journal")
    #print(user_input)
    if any(word in user_input for word in ["add","write","document"]):
        #print("runing add")
        add_journal(user_data)
    
    elif any(word in user_input for word in ["read","view"]):
        read_entery(user_data)

def add_journal(user_data):
    #geting values ready
    now= datetime.datetime.now()
    timestamp = now.strftime("%d%m%y_%H%M%S")
    #print(user_data["journal"])
    #url = f"{os.path.join('data','journals')}journal_{user_data['username']}_{time}.txt" #doesnt work as good
    storage_dir1 = os.path.join("data","journals")
    file_name = f"journal_{user_data["username"]}_{timestamp}.txt"
    url = os.path.join(storage_dir1,file_name)
    user_data["journal"][f"{now}"] = f"{url}"

    #banner
    print("----welcome--to--the--unibot---journal---")
    print("You Can Start Writing And It Will BE Documented Automaticaly")
    print("You can finish the documentating be using '<end>' in your sentence")
    #writing section
    writing = True
    document = []
    while writing:
        context = input()

        #puting the end to writing pannel 
        if "<end>" in context:
            context = context.replace("<end>","").strip()
            document.append(context)
            writing = False
        
        #documanting the line    
        else:
            document.append(context)

    #writing it to file
    with open(url,"w",encoding="utf-8") as file:
        for line in document:
            file.write(line + "\n")
        print(f"--file-writen-to--{url}")
    #print(user_data)

def read_entery(user_data):
    
    #bannner 
    print("----welcome--to--the--unibot---journal---")
    print("Please write the index of journal file you want to read")
    print("Tip: Use -1 for the latest journal, -2 for the previous one.")

    #reading and listing all the enteres
    try:
        n=0
        name_list=[]
        for file_name in user_data["journal"]:
            print(f"{n} --- {file_name}")
            name_list.append(file_name)
            n+=1
        run_input_recever = True
        while run_input_recever:
            input_index = input(":- ")
            try:
                url = user_data["journal"][name_list[int(input_index)]]
                with open(url,"r",encoding = "utf-8") as file:
                    run_input_recever = False
                    contents = file.read()
                    print(contents)
            except IndexError:
                print("enter valid index")
            except ValueError:
                print("please enter a number")

    except:
        print("It seems like you dont have any files to view")

"""
handle("add",{
        "user_id": "1",
        "password": "1234",
        "username": "admin",
        "is_locked": True,
        "budget": [],
        "tasks": {
            "make tea": True
        },
        "contacts": {
            "samar": []
        },
        "grades": [
            {
                "physics": [
                    50.0,
                    40.0
                ],
                "chemistry": [
                    60.0,
                    30.0
                ],
                "math": [
                    70.0,
                    40.0
                ]
            }
        ],
        "journal": {}
    })
"""