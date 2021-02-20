import random
number = random.randrange(1,100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("You need to guess higher. Try again")
        guess = int(input("\nGuess a number between 1 and 100: "))
    else:
        print("You need to guess lower. Try Again")
        guess = int(input("\nGuess a number between 1 and 100: "))

print("You've guessed the number correctly!")