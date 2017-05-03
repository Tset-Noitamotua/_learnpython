"""
contacts_4.py
This program allows me to manage my contacts.
@author Test Noitamotua
@version 2017-05-03
"""


class Person(object):
    """
    The Person class defines a person in terms of a
    name, phone number and email adress.
    """
    # constructor
    def __init__(self, theName, thePhone, theEmail):
        self.name = theName
        self.phone = thePhone
        self.email = theEmail
    # accesser methods (getters)
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email
    # mutator methods (setters)
    def set_name(self, newName):
        self.name = newName
    def set_phone(self, newPhoneNo):
        self.phone = newPhoneNo
    def set_email(self, newEmail):
        self.email = newEmail

    # String method - show a string represantiona of Person object
    def __str__(self):
        return "Person[name=" + self.name + \
               ", phone=" + self.phone + \
               ", email=" + self.email + \
               "]"


# Some functions which are usefull to manage my contacts
# NOTE: this functions do NOT belong to the Person class above
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    print(">>> OK! Added new contact!")
    return Person(name, phone, email)

def lookup_contact(contacts):
    found = 0
    name = input("Enter name to lookup: ")
    for contact in contacts:
        if name in contact.get_name():
            print(contact)
            found += 1
        if not found:
            print("There is no contact with the name '{}'".format(name))

def edit_mult_contacts(matches):
    pass

def edit_contact(contacts):
    match = 0
    matches = []
    name = input("Which contact would you like to edit? ")
    for contact in contacts:
        if name in contact.get_name():
            match += 1
            matches = matches.append(contact)
            edit_mult_contacts(matches)
        
            # print("...found: {}".format(contact))
            # print("Would you like to edit this contact? ")
            # print("1) yes       2) no")
            # option = input("> ")
            # if option == "1" or option == "yes":
            #     print("What do you want to edit?")
            #     print("1) name      2) phone        3) email")
            #     option = input("> ")
            #     if option == "1" or option == "name":
            #         name = input("Type in the new name: ")
            #         contact.set_name(name)
            #         print("Changed contacts's name.")
            #         print(contact)

        if not match:
            print("There is no contact with the name '{}' to edit!".format(name))

def show_all_contacts(contacts):
    for contact in contacts:
        print(contact)


def main():
    contacts = []
    running = True
    while running:
        print("\nMy Contacts Manager (choose an option:)")
        print("1) add new contact       2) lookup contact")
        print("3) edit contact          4) show all contacts")
        print("5) exit")
        option = input("> ")
        if option == "1":
            contacts.append(add_contact())
        elif option == "2":
            lookup_contact(contacts)
        elif option == "3":
            edit_contact(contacts)
        elif option == "4":
            show_all_contacts(contacts)
        elif option == "5" or option == "exit":
            running = False
        else:
            print("Unknown command! Please try again.")


if __name__ == "__main__":
    main()
