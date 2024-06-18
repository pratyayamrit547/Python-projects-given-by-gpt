student_info1={}
student_info2={}
class Student_info:
    def __init__(self,name,std,sec,roll):
        self.name=name
        self.std=std
        self.sec=sec
        self.roll=roll
def add():
    try:
        name=input("give student name:").title()
        std=input("give class of the student:")
        sec=input("give sec of the student:")
        roll=int(input("give roll number of the student:"))
        info=Student_info(name, std, sec, roll)
        information={name:std}
        information1={roll:sec}
        student_info1.update(information)
        student_info2.update(information1)
        print("Data of the student added successfully")
    except ValueError:
        print("Give roll number in number")
def view():
    if len(student_info1)==0:
        print("There is no data of student".title())
    else:
        while True:
            a=input("give name of the student whom details you want:").title()
            for index,i in enumerate(student_info1.items(),1):
                for index,j in enumerate(student_info2.items(),1):
                    if a==i[0]:
                        print(f"the details of the student name {a} :\nclass={i[1]}\nsec={j[1]}\nroll={j[0]}".title())
                        break
                    else:
                        print("the name is not in the database")
                        break
def delete():
    try:
        name = input("give student name:").title()
        std = input("give class of the student")
        sec = input("give sec of the student:")
        roll = int(input("give roll number of the student:"))
        for index, i in enumerate(student_info1.items(), 1):
            for index, j in enumerate(student_info2.items(), 1):
                if name==i[0] and std==i[1]:
                    if sec==j[1] and roll==j[0]:
                        a=input("Are you sure you want to delete it yes/no:".title()).title()
                        if a=="Yes":
                            del (student_info1[name])
                            del (student_info2[roll])
                            print("Deleted successfully")
                        elif a=="No":
                            print("Ok not deleted Your data is safe".title())
                    else:
                        print("Give details of the student correctly")
    except:
        print("Give details of yhe student correctly")
def menu():
    try:
        while True:
            print("\n1.Add data of the student\n2.View data of the student\n3.Delete data of the student\n4.Quit")
            ask=int(input("GIVE INDEX OF THE TASK ACCORDING TO YOUR CHOICE:"))
            if ask==1:
                add()
            elif ask==2:
                view()
            elif ask==3:
                delete()
            elif ask==4:
                break
            else:
                print("Give correct index of the task")
    except ValueError:
        print("Give index in number")
menu()