from secrets import choice

computer = 0
person = 0

for x in range(3):
    print("welcome to rock, paper, scissors!")

    rps_random = ["rock", "paper", "scissors"]

    rps = input("pick the hand you wanna play with: ").lower()

    Random = choice(rps_random)

    while Random == "rock":
        if rps == "scrissors":
            print("the computer has chosen 'ROCK' so you lose! ")
            computer += 1
        elif rps == "rock":
            print("The computer has chosen 'ROCK' too so its a tie!! ")
            computer += 1
            person += 1
        else:
            print("the computer has chosen 'ROCK' so you Win!!! ")
            person += 1
        break
            
    while Random == "paper":
        if rps == "rock":
            print("the computer has chosen 'PAPER' so you lose!! ")
            computer += 1
        elif rps == "paper":
            print("The computer has chosen 'PAPER' too so its a tie!! ")
            computer += 1
            person += 1
        else:
            print("the computer has chosen 'PAPER' so you Win!!! ")
            person += 1
        break

    while Random == "scissors":
        if rps == "paper":
            print("the computer has chosen 'SCISSORS' so you lose! ")
            computer += 1
        elif rps == "scissors":
            print("The computer has chosen 'SCISSORS' too so its a tie!! ")
            computer += 1
            person += 1
        else:
            print("the computer has chosen 'SCISSORS' so you Win!!! ")
            person += 1
        break

#print("the score was:\n"f"{computer} > COMPUTER\n{person} > YOU")

ask1 = input("do you wanna know who the winner is?: (y/n) ")
if ask1 == "y":
    if person > computer:
        print("YOUVE WON!!")
    elif person == computer:
        print("It was a tie :D")
    else:
        print("Computer won!")
else:
    print("Thanks for playing!")
    quit()
