
# STUDY BUDDY APP

# Subjects and their concepts
subjects = {
    "Math": ["geometry", "trigonometry", "algebra"],
    "English": ["reading", "writing", "grammar", "vocab"],
    "Science": ["biology", "chemistry", "physics"],
    "Language": ["spanish", "french", "italian"]
}


# Welcome Page
def welcome():
    print("=" * 40)
    print("       WELCOME TO STUDY BUDDY!")
    print("=" * 40)
    print("Your personal study assistant!")
    print("Find out which subject a concept belongs to.")
    print("=" * 40)


# Search for a concept
def search():
    concept = input("\nEnter a concept: ").strip().lower()

    found = False

    for subject, concepts in subjects.items():
        if concept in concepts:
            print(f"\n{concept} is in {subject}!")
            found = True
            break

    if not found:
        print("\nConcept not found. Please try again.")


# Main Menu
def main():
    welcome()

    while True:
        print("\n------ MAIN MENU ------")
        print("1. Search for a concept")
        print("2. View all subjects")
        print("3. Exit Study Buddy")

        choice = input("\nChoose an option (1-3): ")

        if choice == "1":
            search()

        elif choice == "2":
            print("\nAvailable Subjects:")
            for subject in subjects:
                print(f"- {subject}")

        elif choice == "3":
            print("\nThank you for using Study Buddy!")
            print("Good luck with your studies!")
            break

        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


# Start the app
main()
