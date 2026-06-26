import json
import os

#code for login
def login():
    print("LOGIN SYSTEM")

    path = "data/users/users.json"

    # load users file
    try:
        with open(path, "r", encoding="utf-8") as f:
            users = json.load(f)
    except:
        print("Error loading user database ❌")
        return None

    username = input("Username: ").lower()
    password = input("Password: ")

    # check user exists
    if username in users:
        if users[username]["password"] == password:
            print("Login successful ✔")

            return {
                "user_id" : users[username]["user_id"],
                "password": users[username]["password"],
                "username": username,
                "budget": users[username]["budget"],
                "tasks": users[username]["tasks"],
                "contacts": users[username]["contacts"],
                "grades" : users[username]["grades"],
                "journal" : users[username]["journal"]
            }

    print("Invalid credentials ❌")
    return None