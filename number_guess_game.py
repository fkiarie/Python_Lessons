from curses.ascii import isdigit
import random

top_of_range = input("Type a number: ")
guesses = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter number larger than 0")
        quit()
else:
    print("Enter number please")
    quit()

random_number = random.randint(0,top_of_range)

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    else:
        print("you got it wrong")


print("you got in", guesses, "guesses")