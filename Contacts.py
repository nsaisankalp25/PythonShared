import json

def load_my_contacts(): # Returns a list of contacts
    try:
        path = r"C:\Users\saisa\Desktop\Coding\Course\Students\Commons\depedencies\All_contacts.json"
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_my_contacts(my_contacts):
    path = r"C:\Users\saisa\Desktop\Coding\Course\Students\Commons\depedencies\All_contacts.json"
    with open(path, "w") as file:
        json.dump(my_contacts, file)

def add_my_contact(name, phone, email):
    my_contacts = load_my_contacts() # list
    contact = {"name": name, "phone": phone, "email": email}
    my_contacts.append(contact)
    save_my_contacts(my_contacts)

def display_my_contacts():
    my_contacts = load_my_contacts()
    if not my_contacts:
        print("No contacts found.")
    else:
        print("My Contacts:")
        print(my_contacts)
        for contact in my_contacts:
            print(f"Name: {contact['name']} \n   Phone: {contact['phone']} \n   Email: {contact['email']}")


while True:
    print("\nMy Contact Book")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_my_contact(name, phone, email)
        print("Contact added successfully!")

    elif choice == "2":
        display_my_contacts()

    elif choice == "3":
        print("Exiting My Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")