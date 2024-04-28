# importing os for making list of directories
import os
# importing csv for making csv files and creating and reading it in dictionary
import csv


def login_function():
    """This login_function is used to check is the user have already used password manager or not"""
    # creates list of directories and files present in system
    list_dir = os.listdir()
    while True:
        # opening file in append mode
        with open("Information_of_login_user","a") as file:
            try:
                ask_user = int(input("Type [1] for new user\nType [2] for old user\nType [3] for exiting the code\nGive your action:"))
                # opening new  user function for new users
                if ask_user == 1:
                    new_user(file)
                    print("Give your submitted details in old user interface by clicking [2]")
                # opening existing user file for existing users
                elif ask_user == 2:
                    existing_user(list_dir)
                # it helps for breaking the loop
                elif ask_user == 3:
                    print("You have successfully exited from the password manager")
                    break
                else:
                    print("Give your reply only in [1] and [2]")
            # raising ValueError if user enters any digit rather than numbers
            except ValueError:
                print("Give your reply only in numbers not in alphabets")


def new_user(file):
    """ This function adds user information to Information_of_login_user file. This function uses csv,
    dictionary comprehension and zip function. """
    # heading for the file
    column_header = ["Name", "Password"]
    print("Welcome to password manager set your new password\n")
    name = input("write your name:")
    password = input('Give password:')
    # this is taking user data and insert it in file and fieldnames is the file headline and getting,
    # file name from login user function.
    updating_file = csv.DictWriter(file, fieldnames=column_header)
    # file.tell() is telling the lines present in the file which is helping for creating headline only,
    # one time not two time
    if file.tell() == 0:
        updating_file.writeheader()
    # .writerow() is helping for establishing data is csv format here we are using dictionary comprehension,
    # and zip function for doing it.The work of zip is like this zip([1,2,3],[1,4,9]) output will be 1:2,2:4,3:9,
    # here we can use any data types which can be iterated in zip function
    updating_file.writerow({name: password for (name, password) in zip(column_header, [name, password])})


def existing_user(list_dir):
    """The function of this existing user function is to verify the user and if iit  """
    name = input("write your name:")
    password = input('Give password:')
    # opening file in read mode
    with open("Information_of_login_user", "r") as read_file:
        # reading file in dictionary mode
        reading_file = csv.DictReader(read_file)
        for i in reading_file:
            # parsing name and password from the file
            if i['Name'] == name and i['Password'] == password:
                try:
                    print("Verified that you are a existing user\n")
                    ask_user = int(input("Type [1] for adding password\nType [2] for reading files\nGive your action:"))
                    if ask_user == 1:
                        check_of_dir(name, list_dir)
                    elif ask_user == 2:
                        reader(name)
                    else:
                        print("Give your reply only in [1] and [2]")
                except ValueError:
                    print("Give your reply only in numbers not in alphabets")
        else:
            print("Username and password not matched")


def check_of_dir(name,list_dir):
    """" this is the function which is used to check the file is present or not """
    if name in list_dir:
        # if name is present in directory than sending it in update of manager function
        update_of_manger(name)
    if not name in list_dir:
        # if name is not matched than sending it in creation_of_manager function.
        creation_of_manager(name)

def creation_of_manager( name ):
    """It creates the new file of the user if the file not existed"""
    # opening file in write mode so that it create files if files do not exist in directory.
    file_open1 = open(f"{name}", "w")
    print('Your password manager has been created')
    file_open1.close()


def update_of_manger( name ):
    """This function updates the existing file"""
    print('Your password manager is ready to be updated')
    web_name = input("Give website or app name:")
    userid = input(f"Give your user name which you have given in the {web_name}:")
    password = input(f"Give the password which you have submitted in the {web_name}:")
    # call_of_func is getting the return value of ask_more() function
    call_of_func = adding_more_info()
    # calling the writer function.
    writer(name, web_name, userid, password, call_of_func)


def writer(name, web_name, userid, password, call_of_func):
    """It writes the details of the user in the file in csv format using csv DictWriter"""
    # headline of the file
    column_header = ["Website", 'UserId', "Password", "MoreInfo"]
    # opening file in append mode
    with open(f"{name}", "a") as file:
        writing_file = csv.DictWriter(file, fieldnames=column_header)
        if file.tell() == 0:
            writing_file.writeheader()
        writing_file.writerow({headline: content for (headline, content) in zip(column_header, [web_name, userid, password, call_of_func])})


def reader(name):
    """It reads the file using fileIO"""
    # opening file in read mode and parsing it in Dictionary format
    with open(name, "r") as file:
        a = csv.DictReader(file)
        for i in a:
            print(f'Website name:{i['Website']}\nUser name:{i["UserId"]}\nPassword:{i["Password"]}\nMore Information:\n\'{i["MoreInfo"]}\'\n')


def adding_more_info():
    """This function adds more information of the user in the function if requires"""
    try:
        ask_for_more = input("If you want to add more things then type 'YES' and if you do not want to add then type 'NO':").title()
        if ask_for_more == "Yes":
            action = input("add:")
            return action
        elif ask_for_more == "No":
            print("Ok nothing to be added more")
        else:
            print("Reply either in 'YES' or 'NO'")

    except ValueError:
        print("Reply only in 'yes' or 'no' not in  numbers")


login_function()
