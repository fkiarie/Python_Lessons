print("Welcome to my game!")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions right")
print("You got " + str((score / 4) * 100 )+ "%")