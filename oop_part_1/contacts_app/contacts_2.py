"""
contacts_2.py
This program allows me to manage my contacts.
@author Test Noitamotua
@version 2017-05-03
"""

def main():

    friends = []

    for i in range(2):
        print("Contact Manager")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        friends.append([name, phone, email])

    for i in range(len(friends)):
        print("Contact info")
        for j in range(len(friends[i])):
            print(friends[i][j])

if __name__ == "__main__":
    main()
