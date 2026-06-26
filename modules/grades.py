def handle(user_input, user_data):
    # If the grades list is totally empty, run the setup first!
    if "grades" not in user_data or user_data["grades"] == []:
        setup_subjects(user_data)
        return

    # Chatbot keyword matching
    if "add" in user_input and "subject" in user_input:
        add_subject(user_data)
    if "add" in user_input or "score" in user_input or "enter" in user_input:
        add_marks(user_data)

    elif "edit" in user_input or "change" in user_input:
        edit_marks(user_data)

    elif "delete" in user_input or "remove" in user_input:
        delete_subject(user_data)

    elif "report" in user_input or "show" in user_input or "view" in user_input:
        show_report(user_data)

    elif "stats" in user_input or "analysis" in user_input or "average" in user_input:
        show_stats(user_data)
    else:
        print("🤖: I didn't quite catch that. Do you want to add, edit, delete, show report, or view stats?")


def setup_subjects(user_data):
    print("\n--- Welcome to Grades Setup ---")
    num_input = input("How many subjects do you have?: ")
    
    if not num_input.isdigit():
        print("🤖: Please enter a valid number next time.")
        return
        
    num_subjects = int(num_input)
    
    subjects_dict = {}
    print("\nEnter your subject names:")
    for i in range(num_subjects):
        sub_name = input(f"Subject {i+1}: ").strip().lower()
        if sub_name != "" and sub_name not in subjects_dict:
            subjects_dict[sub_name] = [] 
        else:
            print("⚠️ Skipped: Empty or duplicate.")

    user_data["grades"] = [subjects_dict]
    print("🤖: All set up! Go ahead and ask me to add marks now.")

def add_marks(user_data):
    print("\n--- Adding a New Test Round ---")
    subjects_dict = user_data["grades"][0]
    
    new_round_scores = {}
    print("🤖: Please enter the marks for ALL your subjects:")
    
    for subject in subjects_dict.keys():
        mark_input = input(f"Enter mark for {subject.capitalize()} (0-100): ")
        try:
            mark = float(mark_input)
            if mark >= 0 and mark <= 100:
                new_round_scores[subject] = mark
            else:
                print("⚠️ Out of range! Defaulting to 0.")
                new_round_scores[subject] = 0.0
        except:
            print("⚠️ Not a number! Defaulting to 0.")
            new_round_scores[subject] = 0.0

    for subject, score in new_round_scores.items():
        subjects_dict[subject].append(score)
        
    print("🤖: Successfully added this round of marks for all subjects!")

def add_subject(user_data):
    print("\n--- ➕ Add a New Subject ---")
    subjects_dict = user_data["grades"][0]
    
    new_sub = input("Enter the name of the new subject: ").strip().lower()
    
    if new_sub == "":
        print("🤖: Subject name cannot be empty!")
        return
        
    if new_sub in subjects_dict:
        print("🤖: That subject already exists!")
        return

    # Find out how many test rounds we have already recorded
    first_subject = list(subjects_dict.keys())[0]
    
    if isinstance(subjects_dict[first_subject], list):
        total_rounds = len(subjects_dict[first_subject])
    else:
        total_rounds = 0

    # Give the new subject a list filled with 0.0 for all past rounds
    # This prevents the report card from crashing!
    subjects_dict[new_sub] = []
    for i in range(total_rounds):
        subjects_dict[new_sub].append(0.0)

    print(f"🤖: Successfully added '{new_sub.capitalize()}'! It has been backfilled with 0.0 for past rounds.")

def edit_marks(user_data):
    print("\n--- Edit Marks ---")
    subjects_dict = user_data["grades"][0]

    subject = input("Which subject do you want to edit?: ").strip().lower()

    if subject not in subjects_dict:
        print("🤖: Subject not found.")
        return

    marks_list = subjects_dict[subject]
    if marks_list == []:
        print("🤖: No marks recorded yet for this subject.")
        return

    print(f"Current marks: {marks_list}")
    for i in range(len(marks_list)):
        print(f"Index [{i}]: {marks_list[i]}")

    idx_input = input("Enter the Index number you want to change: ")
    try:
        idx = int(idx_input)
        if idx >= 0 and idx < len(marks_list):
            new_mark = float(input("Enter new mark value: "))
            marks_list[idx] = new_mark
            print("🤖: Updated successfully!")
        else:
            print("🤖: Invalid index number.")
    except:
        print("🤖: Invalid input.")

def delete_subject(user_data):
    print("\n--- Delete Subject ---")
    subjects_dict = user_data["grades"][0]

    subject = input("Enter subject name to delete completely: ").strip().lower()

    if subject in subjects_dict:
        del subjects_dict[subject]
        print(f"🤖: Deleted {subject} from the system.")
    else:
        print("🤖: Subject not found.")

def show_report(user_data):
    print("\n--- View Test Round Report ---")
    subjects_dict = user_data["grades"][0]

    # Quick check: grab the first subject name to see how many rounds exist
    first_subject = list(subjects_dict.keys())[0]
    
    # Safety guard for old integer data
    if not isinstance(subjects_dict[first_subject], list):
        print("🤖: You haven't added any test marks yet! Type 'add marks' to get started.")
        return

    total_rounds = len(subjects_dict[first_subject])

    if total_rounds == 0:
        print("🤖: You haven't added any test marks yet! Type 'add marks' to get started.")
        return

    print(f"🤖: You have {total_rounds} test rounds recorded.")
    user_choice = input("Which test marks do you want me to show? (Type a number, 'last', or 'all'): ").strip().lower()

    # --- 🆕 NEW 'ALL' FEATURE IMPLEMENTATION ---
    if user_choice == "all":
        print("\n=========================================")
        print("          ALL TEST ROUNDS REPORT         ")
        print("=========================================")
        # Loop through every single round index sequentially
        for r_idx in range(total_rounds):
            print(f"--- Test Round {r_idx + 1} ---")
            for subject, marks in subjects_dict.items():
                print(f"  {subject.capitalize()}: {marks[r_idx]}")
            print("-" * 25)
        print("=========================================")
        return  # Exit function early since we already printed everything

    # Determine single index based on input layout
    if user_choice == "last":
        target_idx = -1
    elif user_choice.isdigit() or (user_choice.startswith('-') and user_choice[1:].isdigit()):
        provided_num = int(user_choice)
        if provided_num > 0:
            target_idx = provided_num - 1  # Convert 1 to index 0
        else:
            target_idx = provided_num       
    else:
        print("🤖: I didn't recognize that choice. Showing your latest test marks by default.")
        target_idx = -1

    try:
        print("\n===============================")
        print(f"       TEST ROUND REPORT       ")
        print("===============================")
        for subject, marks in subjects_dict.items():
            print(f"{subject.capitalize()}: {marks[target_idx]}")
        print("===============================")
    except IndexError:
        print("🤖: ❌ That test round index doesn't exist.")

def show_stats(user_data):
    print("\n--- Grade Stats ---")
    subjects_dict = user_data["grades"][0]

    all_marks = []

    for subject, marks in subjects_dict.items():
        if len(marks) > 0:
            sub_avg = sum(marks) / len(marks)
            print(f"{subject.capitalize()} Average: {sub_avg:.1f}")
            for m in marks:
                all_marks.append(m)
        else:
            print(f"{subject.capitalize()} Average: No marks yet")

    print("-" * 30)

    if len(all_marks) > 0:
        overall_avg = sum(all_marks) / len(all_marks)
        highest = max(all_marks)
        lowest = min(all_marks)

        total_squared_diff = 0
        for x in all_marks:
            total_squared_diff += (x - overall_avg) ** 2
        
        variance = total_squared_diff / len(all_marks)
        std_deviation = variance ** 0.5

        print(f"Overall Average: {overall_avg:.1f}")
        print(f"Highest Score: {highest}")
        print(f"Lowest Score: {lowest}")
        print(f"Standard Deviation: {std_deviation:.2f}")
    else:
        print("🤖: No scores found to run stats.")
