import random
print("0:ROCK\n1.PAPER\n2.SCISSOR")
i=0
while i==0:
    try:
        a=int(input("GIVE your attack:").title())
        comp=random.randrange(0,3)
        if comp==0:
            print("you win") if a==1 else print('Match draw') if a==comp else print("Give valid input") if a>2 else print("you lose")
            print("The attack of computer is :",comp)
        elif comp==1:
            print("you win") if a==2 else print("Match draw") if a==comp else print("Give valid input") if a>2 else print("you lose")
            print("The attack of computer is :", comp)
        elif comp==2:
            print("you win") if a==0 else print("Match draw") if a==comp else print("Give valid input") if a>2 else print("you lose")
            print("The attack of computer is :", comp)
        else:
            print("Give value between 0 to 2")
    except:
        print("Give value in int only")
