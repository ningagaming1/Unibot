import json
import hashlib
import uuid
import os

def signup():
    # Define the directory and file path
    dir_path = "data/users"
    file_path = os.path.join(dir_path, "users.json")

    # Automatically create folders if they don't exist yet
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Load existing users or start fresh
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    print("\n=== SIGNUP SYSTEM ===")

    username = input("Username: ").lower().strip()
    if not username:
        print("❌ Username cannot be empty")
        return

    # Everything below is now properly indented inside the function!
    if username in users:
        print("❌ Username already exists")
        return

    password = input("Password: ")
    confirm = input("Confirm Password: ")

    if password != confirm:
        print("❌ Passwords do not match")
        return

    # Create the user profile structure matching your blueprint
    users[username] = {
        "user_id": str(uuid.uuid4()),
        "username": username,
        "password": hashlib.sha256(password.encode()).hexdigest(),
        "budget": [],
        "tasks": {},
        "contacts": [],
        "grades": []
    }

    # Save back to the JSON file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

    print("✔ Account created successfully!")

# This line lets you run the file directly to test it
if __name__ == "__main__":
    signup()