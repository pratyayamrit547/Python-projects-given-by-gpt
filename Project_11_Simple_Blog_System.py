dic= {}
def blog_mng_sys():
    print("1.ADD NEW BLOG\n2.VIEW BLOG\n3.DELETE BLOG")
    try:
        a=int(input("GIVE VALUE ACCORDING TO YOUR REQUIREMENT:"))
        if a >3 :
            print("give correct number only")
        if a==1:
            blog_name=input("give your blog headline name:")
            blog_describe=input("describe your blog::")
            abb=f'the content of the blog name {blog_name} is:-\n  {blog_describe} \n'
            dictionary={blog_name:blog_describe}
            dic.update(dictionary)
        elif a == 2:
            for index, i in enumerate(dic.items(), 1):
                print(f"\t\t\t\t\t\t\t\t{i[0]} \n{i[1]}")

        elif a==3:
            try:
                a = input("Which task you want to delete give it's name:-")
                dic.pop(a)
                for index, i in enumerate(dic, 1):
                    for j in dic.values():
                        print(f'{index}. {i} : {j}')
            except:
                print("give correct task name")
        else:
            print("give correct value")
    except:
            print("please give the integer value from 1 to 3")
            blog_mng_sys()

blog_mng_sys()
while True:
    i=input("Do you want to (restart=r.py or quit=q) the Blog manager system:").title()
    if i == "R":
        blog_mng_sys()
    elif i == 'Q':
        print("You have successfully exit the Blog system manager")
    else:
        print("give correct value")
