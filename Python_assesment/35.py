# Q35. Develop a contact management system
# using list and dictionary where users can
# add, update, search, and delete contacts.

contacts = {}

while True:

    print("\n----- Contact Management Menu -----")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    # add contact
    if choice == 1:

        name = input("Enter name : ")
        number = input("Enter phone number : ")

        contacts[name] = number

        print("Contact Added Successfully")

    # update contact
    elif choice == 2:

        name = input("Enter contact name : ")

        if name in contacts:

            number = input("Enter new phone number : ")

            contacts[name] = number

            print("Contact Updated")

        else:

            print("Contact Not Found")

    # search contact
    elif choice == 3:

        name = input("Enter contact name : ")

        if name in contacts:

            print("Name :", name)
            print("Phone Number :", contacts[name])

        else:

            print("Contact Not Found")

    # delete contact
    elif choice == 4:

        name = input("Enter contact name : ")

        if name in contacts:

            del contacts[name]

            print("Contact Deleted")

        else:

            print("Contact Not Found")

    # exit
    elif choice == 5:

        print("Exiting Program")
        break

    else:

        print("Invalid Choice")