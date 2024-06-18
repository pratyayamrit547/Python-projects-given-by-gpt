import random

a = random.randrange(0, 10)
print(a)
def guess(a):
    b=input("give your number: ")
    if len(b)>1 or len(b)<1:
        print("give one value")
    else:
        c=int(b)
        if c==a:
            print("you have guessed the number")
            a = random.randrange(0, 10)
            print(a)
            guess(a)
        else:
            print("you have not guessed the number")
            print("you have lost one chance")
chance=3
while chance>=1:
    guess(a)
    chance = chance - 1
    if chance==0:
        print("GAME OVER")