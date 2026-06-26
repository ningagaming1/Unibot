import os
import subprocess
import sys

BASE_PATH = r"D:\unibot"

# -----------------------------
# Install required packages
# -----------------------------
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Installing dependencies...")

try:
    install("pyfiglet")
except Exception as e:
    print("Failed to install pyfiglet:", e)

# -----------------------------
# Folder structure
# -----------------------------
folders = [
    "core",
    "auth",
    "modules",
    "files",
    "admin",
    "data/users",
    "data/logs",
    "data/files_inbox",
    "data/files_sorted/pdf",
    "data/files_sorted/txt",
    "data/files_sorted/images",
    "data/files_sorted/books",
    "data/files_sorted/tests",
    "assets"
]

files = {
    "main.py": "",
    "config.py": "",
    "core/router.py": "",
    "core/chatbot.py": "",
    "core/utils.py": "",
    "auth/login.py": "",
    "auth/signup.py": "",
    "modules/budget.py": "",
    "modules/todo.py": "",
    "modules/contacts.py": "",
    "modules/journal.py": "",
    "modules/dice.py": "",
    "files/organizer.py": "",
    "admin/panel.py": "",
    "admin/debug.py": "",
    "assets/help.txt": "",
    "assets/commands.json": ""
}

# -----------------------------
# Create folders
# -----------------------------
for folder in folders:
    path = os.path.join(BASE_PATH, folder)
    os.makedirs(path, exist_ok=True)

# -----------------------------
# Create files
# -----------------------------
for file_path, content in files.items():
    full_path = os.path.join(BASE_PATH, file_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("\nSetup complete! SmartAssistant created at D:\\unibot")