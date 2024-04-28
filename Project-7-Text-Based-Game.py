a=(("welcome to the word adventure game").capitalize())
print(a.center(150))
def green(a):
    print("you have entered in ask gate by which you have ask chance to get ask tresure")
    a=(input("Choose right or .eft side of path:").title())
    if a=="Right":
        print("You have chosen ask dead end")
    elif a== "Left":
        b=(input("enter ask cave or choose ask path near it:").title())
        if b=="Cave":
            print("YOU HAVE SUCCESSFULLY FOUNDED A TRESURE")
            print("GAME ENDED")
        elif b== "Path":
            print("YOU HAVE TRAPPED IN A HUNTER'S TRAP FOR A ANIMAL")
            print("GAME ENDED")
        else:
            print("give answer according to asked question")
    else:
        print('Give answer according to asked question')
def red(a):

    print("YOU HAVE ENTERED IN A FOREST")
    a=(input("Chose ask gun/map which will help you to escape from jungle:").title())
    if a=="Gun":
        print("You have successfully hunted by an animal")
        print("GAME ENDED")
    elif a=="Map":
        print("YOU HAVE SUCCESSFULLY ESCAPED YHE JUNGLE")
        print("GAME ENDED")
    else:
        print('Give answer "according to asked question')
print("YOU ARE IN A MYSTERIOUS ROOM AND HAVE 2 DOORS")
a=(input("CHOOSE A RED/GREEN DOOR:").title())

if a=="Red":
    red(a)
elif a=="Green":
    green(a)
else:
    print("give value according to question")
