class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, contact, new_phone, new_email, new_address):
        contact.phone = new_phone
        contact.email = new_email
        contact.address = new_address

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter a Name: ")
            phone = input("Enter a Phone Number: ")
            email = input("Enter email id: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search results:")
                for idx, result in enumerate(results, start=1):
                    print(f"{idx}. Name: {result.name}, Phone: {result.phone}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            contact_book.view_contacts()
            try:
                contact_idx = int(input("Enter the contact number to update: ")) - 1
                contact = contact_book.contacts[contact_idx]
                new_name = input("Enter new name")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact_book.update_contact(name, contact, new_phone, new_email, new_address)
                print("Contact updated.")
            except (ValueError, IndexError):
                print("Invalid contact number.")
        elif choice == '5':
            contact_book.view_contacts()
            try:
                contact_idx = int(input("Enter the contact number to delete: ")) - 1
                contact = contact_book.contacts[contact_idx]
                contact_book.delete_contact(contact)
                print("Contact deleted.")
            except (ValueError, IndexError):
                print("Invalid contact number.")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()