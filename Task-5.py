contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for name, details in contacts.items():
                print(f"\nName: {name}")
                for key, value in details.items():
                    print(f"{key}: {value}")

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(contacts[search])
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter contact name to update: ")
        if name in contacts:
            contacts[name]["Phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")
            print("Contact updated!")
        else:
            print("Contact not found!")

    elif choice == "5":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")