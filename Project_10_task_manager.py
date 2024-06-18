dic= {}
def task_manager():
    """This code will just simple act like a to do list"""
    print("1.ADD TASK\n2.VIEW TASK\n3.DELETE TASK")
    try:
        a=int(input("GIVE VALUE ACCORDING TO YOUR REQUIREMENT:"))
        if a > 3:
            print("give correct number only")
        if a==1:
            while True:
                b=input("give your task name:")
                bb=input("give description about it:")
                try:
                    bbb=int(input("deadline of the task:"))
                    abb=f'the description of the {b} task is:-\n  {bb} \nthe deadline of the task:-\n  {bbb}'
                    dictionary={b:abb}#this is the dictionary of it
                    dic.update(dictionary)#we are updating above dictionary
                    break
                except Exception as e:
                    print(f"give correct value The error in it:\n{e}")
        elif a==2:
            for index,i in enumerate(dic.items(),1):
                print(f"{index}. the task name is {i[0]} and the description is {i[1]}")#i gets both key and value so just we are takingi[0]] as key and i[1] as value

        elif a==3:
            try:
                while True:
                    a = input("Which task you want to delete give it's name:-")
                    dic.pop(a)
                    for index, i in enumerate(dic, 1):
                        for j in dic.values():
                            print(f'{index}. {i} : {j}')
                    break
            except Exception as e:
                print(f"give correct task name , The error in it :\n{e}")
            else:
                print("give correct value")
    except Exception as e:
        print(f"please give value only in between (1 to 3) integer the error is in it:\n{e}")
task_manager()
while True:
    i=input("Do you want to (restart=r.py or quit=q) the task manager:").title()
    if i=="R":
        task_manager()
    elif i=='Q':
        print("You have successfully exit the task manager")
    else:
        print("give correct value")
