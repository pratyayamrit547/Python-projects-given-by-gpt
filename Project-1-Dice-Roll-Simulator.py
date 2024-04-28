import random
user_input=int(input("Give your opinion:"))
comp_input=random.randrange(0,7)
if user_input==comp_input:
    print("You won")
    print(f"Computer move was:{comp_input}")
else:
    print("you lose")
    print(f"The computer move was:{comp_input}")
