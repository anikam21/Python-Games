import random

user_wins = 0 
computer_wins = 0 
options = ['rock', 'paper', 'scissor']

while True: 
    user_input = input(" Welcome to the game! Type Rock/Paper/Scissors or Q to quit:" + "\n").lower()
    print(user_input)

    if user_input == 'q' : 
        break

    elif user_input not in options:
        print("Invalid! Please type in another response" + "\n")
        continue 

    random_number = random.randint(0, 2)
    
    # rock: 0, paper: 1, scissors: 2 
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_wins+=1

    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_wins+=1

    elif user_input == 'scissor' and computer_pick == 'paper':
        print("You won!")
        user_wins+=1

    else: 
        print("Computer won!")
        computer_wins+=1

print("You won: ", user_wins)
print("Computer won: ", computer_wins)
