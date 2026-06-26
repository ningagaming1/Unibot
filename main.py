#importing all the necessary modules and functions
from auth.login import login
from core.router import route
import os
import pyfiglet
import time
import json

#--------banner---------
def banner():
    clear_screen()
    print(pyfiglet.figlet_format("U N I B O T"))
    print("Smart Student Assistant System")

#----------load------------    
def load_users():
    with open("data/users/users.json", "r", encoding="utf-8") as f:
        return json.load(f)


# ---------- SAVE ----------
def save_users(users):
    with open("data/users/users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

#-----clear screen---------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#--------main file----------
def main():
    banner()
    print("Starting system...\n")


    user_data = login()

    if not user_data:
        print("login Failed")
        counter = 5
        for n in range(5):
            counter-=1
            time.sleep(1)
            print(f"redirecting in {counter}sec")
            if counter == 0:
                break
        return
        

    clear_screen()
    print("Login successful ✔")
    time.sleep(3)
    clear_screen()
    banner()
    print("Type 'exit' to quit\n")

    # CHAT LOOP
    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("saving data....")
            time.sleep(0.25)
            print("Goodbye 👋")
            time.sleep(0.25)
            users = load_users()          # Reload latest file
            users[user_data["username"]] = user_data   # Update only active user
            save_users(users)
            break
        

        if user_input == "clear":
            clear_screen()
            banner()
        
        if user_input =="shut down":
            print("saving data....")
            time.sleep(0.25)
            print("Goodbye 👋")
            time.sleep(0.25)
            users = load_users()          # Reload latest file
            users[user_data["username"]] = user_data   # Update only active user
            save_users(users)
            return "shut down"
        
        else:
            route(user_input, user_data)


if __name__ == "__main__":
    while True:
        out = main()
        if out == "shut down":
            break