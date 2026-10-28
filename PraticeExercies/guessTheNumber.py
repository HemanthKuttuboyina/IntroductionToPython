import random

attempts = 0

while attempts < 7:
    nmbr = random.randint(1,100)
    userGuess = int(input("Enter your guessed number: "))
    if nmbr == userGuess:
        print(f"Bravo! Fount it in {attempts}")
        break
    
    attempts+=1
if attempts == 7:
    print("You Lost ! IDT")