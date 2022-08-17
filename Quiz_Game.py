score = 0
your_score = "Your score is: "
total_score = "Your total score is: "

print("Welcome to my computer quiz!")

name = input("What's your name player? ")
name = name.capitalize()
print("Nice to meet you " + name)
ready = input("Are you ready to play? ")
ready = ready.lower()

if ready != "yes":
    print("Ok , bye")
    quit()

print("Okay! , lets get ready to start :)")

answer1 = input("What does CPU stand for? ")
answer1 = answer1.lower()
if answer1 == "central processing unit":
    score += 1
    print('Correct!')
    print(f"{your_score} {score}")
else:
    print("Incorrect! No points sorry :(")

answer2 = input("What does GPU stand for? ")
answer2 = answer2.lower()
if answer2 == "graphics processing unit":
    score += 1
    print('Correct!')
    print(f"{your_score} {score}")
else:
    print("Incorrect! No points sorry :(")

answer3 = input("What does RAM stand for? ")
answer3 = answer3.lower()
if answer3 == "random access memory":
    score += 1
    print('Correct!')
    print(f"{your_score} {score}")
else:
    print("Incorrect! No points sorry :(")

answer4 = input("What does PSU stand for? ")
answer4 = answer4.lower()
if answer4 == "power supply":
    score += 1
    print('Correct!')
    print(f"{your_score} {score}")
else:
    print("Incorrect! No points sorry :(")

answer5 = input("What does WIFI stand for? ")
answer5 = answer5.lower()
if answer5 == "wireless fidelity":
    score += 1
    print('Correct!')
    print(f"{your_score} {score}")
else:
    print("Incorrect! No points sorry :(")

score = str(score)
print(f"{total_score } {score}")
print("You got " + str(score) + " questions correct!")
score = int(score)
print("You got " + str((score / 5) * 100) + "%")



