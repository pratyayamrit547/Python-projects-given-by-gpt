# SYSTEM BAN GYA HAI BAS OS MODULE AUR FILO IO USE KARNA OS MODULE SE EK DIRECTORY BANANA HAI JIS ME HAR DAY KE WORK KO STORE KARENGE
# AUR FILE IO SE ESSE OPEN CLOSE READ ME MADAD HOGA
print("personal diary".upper().center(150))
dates_of_diary={}
def add():
    try:
        while True:
            date=int(input("Give year in 20xx:"))
            date1=int(input("Give month in 1to12:"))
            date2=int(input("Give today date:"))
            time_of_entry=f"{int(date2)}.{int(date1)}.{int(date)}"
            information=input("Write About Of Today Events:\n")
            data={time_of_entry:information}
            dates_of_diary.update(data)
            print("The today entry has been successfully added")
            break
    except Exception as e:
        print(f"give time in int and the error in you input:{e}")
def view():
    if len(dates_of_diary)==0:
        print("There is no entry in the personal diary")
    else:
        for index,i in enumerate(dates_of_diary.items(),1):
            print(f"{index}.\t\t\t\t\t\t\t\t{i[0]}\n{i[1]}")
def delete_entry():
    while True:
        try:
            delete_input=input("Give date of the entry to be deleted:")
            str(delete_input)
            for index, i in enumerate(dates_of_diary.items(), 1):
                    if i[0] == delete_input:
                        del dates_of_diary[delete_input]
                        print("The data has been successfully deleted")
                        break
                    else:
                        print("give correct input of delete entry of diary")
        except ValueError:
            print("please give correct date")

while True:
    try:
        print("\n1.Add data entry\n2.View data entry\n3.Delete data entry\n4.Quit")
        ask=int(input("Give input according to your preferred task:"))
        if ask==1:
            add()
        elif ask==2:
            view()
        elif ask==3:
            delete_entry()
        elif ask==4:
            print("You have successfully exited from the personal diary entry")
            break
        else:
            print("Give value between 1to4")
    except ValueError:
        print("give value in integer")
