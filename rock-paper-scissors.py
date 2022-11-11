import random

random_number = random.randint(1, 3)

ii = ""

if random_number == 1:
    ii = "Stone"
elif random_number == 2:
    ii = "Scissors"
elif random_number == 3:
    ii = "Paper"

print("If you want to choose stone write 1.\nIf you want to choose Scissors write 2\nIf you want to choose paper write 3")
while True:
    user_answer = int(input())
    if user_answer == 1:
        print("You choose: stone")
        print("Your opponent choose: " + ii)
        if ii == "Stone":
            print("Its draw")
        elif ii == "Scissors":
            print("You won")
        elif ii == "Paper":
            print("You lose")
        break
    if user_answer == 2:
        print("You choose: scissors")
        print("Your opponent choose: " + ii)
        if ii == "Stone":
            print("You lose")
        elif ii == "Scissors":
            print("Its draw")
        elif ii == "Paper":
            print("You won")
        break
    if user_answer == 3:
        print("You choose: paper")
        print("Your opponent choose: " + ii)
        if ii == "Stone":
            print("You won")
        elif ii == "Scissors":
            print("You lose")
        elif ii == "Paper":
            print("Its draw")
        break
    else:
        print("Wrong number, try again")