from curses.ascii import isdigit
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Enter number larger than 0")
        quit()
else:
    print("Enter number please")
    quit()

random_number = random.randrange(-2, 11)
