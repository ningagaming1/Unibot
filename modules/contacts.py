import os
import phonenumbers

def handle(user_input,user_data):
    if any(word in user_input for word in tuple([" add "," insert "])):
        #print("runing add")
        add_contact(user_data)
        #print("run complete add")
    elif any(word in user_input for word in tuple([" remove "," subtract "])):
        #print("runing remove")
        remove_contact(user_data)
        #print("run remove complete")
    elif any(word in user_input for word in tuple([" view "," ponder "])):
        #print("runing view")
        view_contact(user_data)
        #print("run view complete")

def add_contact(user_data):
    #print(user_data)
    #print(user_data["contacts"])
    
    print("please enter the name you want to add :-")
    name = input().lower()
    if name in user_data["contacts"]:
        clear_screen()
        print("The name provided already exists.")
        
        not_exists = True
        while not_exists:
            print("do you want to add another number (y/n)")
            user_input1 =  input().lower()
            if user_input1 == "y":

                clear_screen()
                print("please enter the the number you want to add (with country code):-")
                number = input()

                try :
                    parsed = phonenumbers.parse(number,None)
                    if phonenumbers.is_valid_number(parsed):
                        #print(parsed)
                        user_data["contacts"][name].append(number)
                        list_of_numbers = list(user_data["contacts"][name])
                        set_of_numbers = set(list_of_numbers)
                        user_data["contacts"][name] = list(set_of_numbers)
                        not_exists = False
                    else:
                        print("That doesn't look like a valid phone number. Try again.")

                except phonenumbers.NumberParseException:
                    print("Could not parse that number. Make sure it includes the country code, e.g. +91...")
 
            elif user_input1 == "n":
                print("number not added")
                break

            else:
                clear_screen()

    else:
        print(f"adding {name}")
        print("please add the phonenumber")
        number = input(":-")
        try:
            parsed = phonenumbers.parse(number)
            if phonenumbers.is_valid_number(parsed):
                print(parsed)
                user_data["contacts"][name] = list()
                user_data["contacts"][name].append(number)
                list_of_numbers = list(user_data["contacts"][name])
                set_of_numbers = set(list_of_numbers)
                user_data["contacts"][name] = list(set_of_numbers)
            else:
                print("That doesn't look like a valid phone number. Try again.") 
        except:
            print("Could not parse that number. Make sure it includes the country code, e.g. +91...")

def remove_contact(user_data):
    print("runing")
    count = 0
    name_list = []
    for contact_name in user_data["contacts"]:
        print("Select the index of number you want to remove")
        print(f"{count}.  {contact_name}")
        name_list.append(contact_name)
        count+=1
    index = input(":-")
    try:
        index = int(index)
        clear_screen()
        del user_data["contacts"][name_list[index]]
    except:
        print("seems like there was an error try again")

def view_contact(user_data):
    #print("runing 1")
    count = 0
    name_list = []
    for contact_name in user_data["contacts"]:
        print("Select the index of number you want to view")
        print(f"{count}.  {contact_name}")
        name_list.append(contact_name)
        count+=1
    index = input(":-")
    try :
        index = int(index)
        clear_screen()
        print(f"----------{name_list[index]}---------")
        for number in user_data["contacts"][name_list[index]]:
            print(f"  {number}")
    except:
        print("index found to be non integer")
        print("please retry")

def clear_screen():
    os.system("cls" if os.name== "nt" else "clear")


"""
handle(input(), {
        "user_id": "1",
        "password": "1234",
        "is_locked": True,
        "username": "admin",
        "budget": [],
        "tasks": {
            "make tea": True
        },
        "contacts": {"samar":["+910000000000","+911111111111"]},
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