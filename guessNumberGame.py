import random, sys

target = random.randint(1,20)

for i in range (5,0,-1):
    print("Guess a number between(1-20) you have "+str(i)+" attempts")
    guess = int(input())

    if guess<target:
        print("Your guess is low")

    elif guess>target:
        print("Your guess is high")

    else:
        print("Congratulations! you guess the number :",target)
        sys.exit()

print("Sorry! You can't guess the number in 5 attempts number was:",target)