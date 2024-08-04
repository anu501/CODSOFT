class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return  # Exit the loop once the contact is found and removed
        print("Contact not found")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contact(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)


def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add contact")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Display all contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added")
        elif choice == "2":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted")
        elif choice == "3":
            name = input("Enter the name to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print("Contact found:")
                print(contact)
            else:
                print("Contact not found")
        elif choice == "4":
            print("\nAll contacts:")
            contact_book.display_contact()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
