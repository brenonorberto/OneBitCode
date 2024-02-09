from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete all contacts")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

main()