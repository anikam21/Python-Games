import random

random.randrange(0,10)
random_number = random.randint(0,10)

score = 0
while True:
    score +=1

    user_input = input("Guess the number: ")
    if user_input.isdigit():
        user_input = int(user_input)

        if user_input <= 0:
            print("Please type a number greater than 0 next time")

    else:
        print("Please type a number next time")
        continue
    
    if(random_number == user_input):
        print("Congratulations! You got the number")
        break
    elif user_input > random_number:
        print("You were above the number")
    else:
        print("You were below the number")
            

print("It took you" ,score, "tries")