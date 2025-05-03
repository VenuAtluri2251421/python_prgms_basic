import random
number=random.randint(1,10)
guess=0
while guess!=number:
    guess=int(input("guess a number"))
    if guess==number:
        print("you got it")
        break
    elif guess<number:
        print("go higher")
    else:
        print("go lower")
