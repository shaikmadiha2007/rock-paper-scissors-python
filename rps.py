import random
print("welcome to rock paper scissors game")
choices = ["rock","paper","scisssors"]
user = input("enter rock, paper or scissors: ").lower()
computer = random.choice(choices)

print("computer:",computer)
#tie case
if user == computer:
    print("it is a Tie")

#ur winning cases
elif user == "rock" and computer == "scissors":
    print("you win")

elif user == "paper" and computer == "rock":
    print("you win")

elif user == "scissors" and computer == "paper":
    print("you win")

#compuer winning cases

elif computer == "rock" and user == "scissors":
    print("you win")

elif computer == "paper" and user == "rock":
    print("you win")

elif computer == "scissors" and user == "paper":
    print("you win")

#invalid input
else:
    print("Invalid input")