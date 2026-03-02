# This is a Snake, Water and Gun Game python code. Run, Play and See how it's work.
'''1 for snake
    -1 for water
    0 for gun'''

import random
computer = random.choice([-1,1,0]) # It will randomize the value of computer variable.

younum = input("Let's play snake, water and gun game!\nEnter your choose by it's first small letter: ")

# What computer choose.
computerdict ={1:"Snake", -1:"Water", 0:"Gun"}
print(f"Computer choose {computerdict[computer]}")

# What you choose
youdict = {"s":1, "w":-1, "g":0}
you = youdict[younum]
print(f"You choose {computerdict[you]}")

# All condition of game.
if(computer==you):
    print("It's a Draw!")
else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You lose!")
    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==0 and you==1):
        print("You lose!")
    elif(computer==0 and you==-1):
        print("You win!")
        