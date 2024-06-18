print((("contact database").swapcase()).center(150))
def add_contact():
    try:
        try:
            name = input("give name:")
            number = int(input("give number:"))
            str_number=str(number)
            if len(str_number)==10:
                b = {name: number}
                details.update(b)
                print("The mobile data is successfully added")
            else:
                print("Give mobile number in 10 digits")
        except ValueError:
            print("give numbers in integer and name in strings")
    except Exception as e:
        print(f"The problem in your input is:-\n{e}")
def view_contact():
    for index, i in enumerate(details.items(), 1):
        if len(details) == 0:
            print("there is no details stored in the database")
        else:
            print(f"{index}. {i[1]} is the number of {i[0]}")
def delete_contact():
    try:
        a = input("Type name of the contact person:")
        del (details[a])
        print("The mobile data is successfully deleted")
    except:
        print("The name of the contact person is not available")
details={}
while True:
    try:
        print("\n1.add contacts\n2.view contacts\n3.delete contacts\n4.quit".title())
        choice= int(input("choose your preferred task:"))
        if choice==1:
            add_contact()
        elif choice==2:
            view_contact()
        elif choice==3:
            delete_contact()
        elif choice==4:
            print("You have successfully exited the database")
            break
        else:
            print("give correct value")
    except:
        print("give correct value")