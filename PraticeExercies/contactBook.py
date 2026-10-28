contacts = {'hemanth':[{'phone':[]},{'email':[]}]}
while True:
    option = input("1 to Add 2 to Search 3 to exit: ")
    if option == "1":
        print("Add a contact")
        name = input("Enter Contact Name: ")
        totalPhoneOfNumbers = int(input("Enter number of phoneNumbers you want to insert: "))
        phone = []
        for i in range(totalPhoneOfNumbers):
            phoneNumbers = input("Enter the PhoneNumber: ")
            phone.append(phoneNumbers)
    
        email = input("Enter Email: ")
    
        phoneBook = {'phone':phone}
        emailBook = {'email':email}
        if name in contacts:
            contacts[name][0]['phone'].append(phone)
            contacts[name][1]['email'].append(email)
        contacts[name] = [phoneBook,emailBook]
        adding = int(input("Enter 0 to exit 1 to add new Contact :"))
    if option == "2":
        searchName = input("Enter the Name: ")
        if searchName in contacts:
            print(f"Name :{searchName:<5}")
            print(f"Contacts :{contacts[searchName][0]['phone']}")
            print(f"email :{contacts[searchName][1]['email']}")
        else:
            print("Contact not Found !!!")
        search = bool(input("Enter False to Stop: "))
    if option == "3":
        break
    