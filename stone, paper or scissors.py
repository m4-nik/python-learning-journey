#building a stone , paper & scissors game
import random
AI = ["stone", "paper", "scissors"]
User = input("Stone, Paper or Scissors?")
x = random.choice(AI)
print (x)
if x == User.lower():
    print ("Its a draw")
elif x == "stone" and User.lower()=="paper":
    print ("You won :O")
elif x == "stone" and User.lower()=="scissors":
    print ("You lost :(")
elif x == "paper" and User.lower()=="scissors":
    print ("You won :O")
elif x == "paper" and User.lower()=="stone":
    print ("You lost :(")
elif x == "scissors" and User.lower()=="paper":
    print ("You lost :(")
elif x == "scissors" and User.lower()=="stone":
    print ("You won :O")
else:
    print("Invalid input")
