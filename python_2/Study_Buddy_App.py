
#STUDY BUDDY APP


# CONSTANTS
MAX_HISTORY = 5
import os

HISTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "study_buddy_history.txt")

# Subjects and their concepts
subjects = {
    "Math": ["geometry", "trigonometry", "algebra"],
    "English": ["reading", "writing", "grammar", "vocab"],
    "Science": ["biology", "chemistry", "physics"],
    "Language": ["spanish", "french", "italian"]
}

# WELCOME PAGE
def welcome():
    print("=" * 40)
    print("       WELCOME TO STUDY BUDDY!")
    print("=" * 40)
    print("Your personal study assistant!")
    print("Find out which subject a concept belongs to.")
    print("=" * 40)

# FIND A CONCEPT'S SUBJECT
def find_subject(concept, subject_data):
    for subject, concepts in subject_data.items():
        if concept in concepts:
            return subject

    return None


# MANAGE SEARCH HISTORY
def add_to_history(concept, history):
    history.append(concept)

    # Keep only the five most recent searches
    if len(history) > MAX_HISTORY:
        history.pop(0)

    # Return the current number of saved searches
    return len(history)


# READ SEARCH HISTORY FROM FILE
def load_search_history(history):
    file = None

    try:
        file = open(HISTORY_FILE, "r", encoding="utf-8")

        for line in file:
            concept = line.strip()

            if concept:
                history.append(concept)

        # Keep only the five most recent searches
        while len(history) > MAX_HISTORY:
            history.pop(0)

    except FileNotFoundError:
        print("\nNo previous search history found.")

    except OSError:
        print("\nUnable to read the search history.")

    else:
        if history:
            print("\nPrevious search history loaded!")

    finally:
        if file is not None:
            file.close()


# SAVE SEARCH HISTORY TO FILE

def save_search_history(history):
    file = None

    try:
        file = open(HISTORY_FILE, "w", encoding="utf-8")

        for concept in history:
            file.write(concept + "\n")

    except OSError:
        print("\nUnable to save search history.")

    else:
        print("\nYour search history was saved!")

    finally:
        if file is not None:
            file.close()


# SEARCH FOR A CONCEPT
def search(subject_data, history):
    concept = input("\nEnter a concept: ").strip().lower()

    found_subject = find_subject(concept, subject_data)

    if found_subject is not None:
        print(f"\n{concept} is in {found_subject}!")

        history_count = add_to_history(concept, history)

        print("Search added to your recent history!")

    else:
        print("\nConcept not found. Please try again.")


# MAIN MENU
def main():
    welcome()

    # Load previous searches when the app starts
    search_history = []
    load_search_history(search_history)

    while True:
        print("\n------ MAIN MENU ------")
        print("1. Search for a concept")
        print("2. View all subjects")
        print("3. Exit Study Buddy")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            search(subjects, search_history)

        elif choice == "2":
            print("\nAvailable Subjects:")

            for subject, concepts in subjects.items():
                print(f"- {subject}: {', '.join(concepts)}")

        elif choice == "3":
            print("\nThank you for using Study Buddy!")
            print("Good luck with your studies!")

            # Save searches before exiting
            save_search_history(search_history)

            break

        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


# ==========================================
#             START THE APPLICATION
# ==========================================

main()
