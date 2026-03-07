from random import randint

x = randint(1,100)
print("-----Let's play a Game-----")
print("A Child think a number between 1 to 100")


g = -1
guess = 0
while(g!=x): # Till Now the 'g = -1', so it entered in while loop
    g = int(input("Guess the Correct Number: "))
    if(g>x):
        print("Lower the Number!")
    elif(g<x):
        print("Higher the Number!")  
    guess +=1

print(f"You Got the Right Guess {x}!! in {guess}th attempt")
