import os
import time

# Define the storage directory path globally at the top of your file
STORAGE_DIR = os.path.join("data", "journals")

def handle(user_input, user_data):
    """
    This is the function called by your main router.
    It inspects the command string to route the action locally.
    """
    user_input = user_input.lower().strip()

    # Crucial step: Ensure the sub-dictionary exists in user_data so we don't get KeyErrors
    if "journal" not in user_data:
        user_data["journal"] = {}

    # Local token checks
   
    if "write" in user_input or "new entry" in user_input:
        create_entry(user_data)
    elif "read" in user_input or "view" in user_input:
        read_entry(user_data)
    else:
        # Fallback if they just type "journal" without an action verb
        print("\n📔 --- Personal Journal Module ---")
        print("Commands: 'write journal' or 'read journal'")


def create_entry(user_data):
    username = user_data.get("username", "default")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    readable_time = time.strftime("%d-%m-%Y %H:%M:%S")
    
    # Ensure the directory path exists on the system before trying to write files
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
        
    print("\n✍️ Write your thoughts below. Press Enter when finished:")
    content = input(":- ").strip()
    
    if not content:
        print("⚠️ Entry was empty. Nothing saved.")
        return

    # Combine the storage directory with your user-specific file naming layout
    filename = os.path.join(STORAGE_DIR, f"journal_{username}_{timestamp}.txt")
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
            
        # Store the complete relative path in the index so read_entry knows exactly where to look
        user_data["journal"][readable_time] = filename
        print(f"💾 Saved successfully to {filename}!")
        
    except Exception as e:
        print(f"❌ File saving operation failed: {e}")


def read_entry(user_data):
    if not user_data["journal"]:
        print("📔 Your journal index is empty!")
        return

    print("\n📅 Available Journal Entries:")
    print("-" * 40)
    timestamps_list = list(user_data["journal"].keys())
    
    for index, readable_time in enumerate(timestamps_list):
        print(f"[{index}] {readable_time}")
    print("-" * 40)
    
    try:
        choice = input("Enter the number of the entry you want to read: ").strip()
        idx = int(choice)
        
        if 0 <= idx < len(timestamps_list):
            target_time = timestamps_list[idx]
            target_file = user_data["journal"][target_time]
            
            # Open the file directly from the path stored in your json registry
            if os.path.exists(target_file):
                with open(target_file, "r", encoding="utf-8") as file:
                    print(f"\n📖 Entry from {target_time}:")
                    print("=" * 40)
                    print(file.read())
                    print("=" * 40)
            else:
                print(f"❌ The file could not be found at {target_file}")
        else:
            print("❌ Invalid entry number.")
            
    except (ValueError, IndexError):
        print("❌ Invalid input selection.")