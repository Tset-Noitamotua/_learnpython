"""
contacts_3.py
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
    def set_phone(self, newPhoneNo):
        self.phone = newPhoneNo

    def set_email(self, newEmail):
        self.email = newEmail

    def __str__(self):
        return "Person[name=" + self.name + \
               ", phone=" + self.phone + \
               ", email=" + self.email + \
               "]"

def main():

    friend1 = Person("Jill", "12345", "jill@mail.com")
    print(friend1.get_email())
    friend1.set_email("jill.sanders@gmail.com")
    print(friend1.get_email())
    print(friend1)


if __name__ == "__main__":
    main()
