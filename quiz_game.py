print("Welcome to my Computer Quiz!")
playing = input("Do you want to play? Type (yes/no) ")

if(playing.lower() != "yes"):
    quit()
print("Okay! Let's play!")

score = 0
questions = 0

answer = input("What does CPU stand for? ")
questions +=1
if (answer.lower() != "central processing unit"):
    print("Wrong answer!") 
else: 
    print("Right Anwer!")
    score +=1 

answer = input("What does GPU stand for? ")
questions +=1
if (answer.lower() != "graphics processing unit"):
    print("Wrong answer!") 
else: 
    print("Right Anwer!")
    score +=1 

answer = input("What does RAM stand for? ")
questions +=1
if (answer.lower() != "random access memory"):
    print("Wrong answer!") 
else: 
    print("Right Anwer!")
    score +=1 


answer = input("What does PSU stand for? ")
questions +=1
if (answer.lower() != "power supply unit"):
    print("Wrong answer!") 
else: 
    print("Right Anwer!")
    score +=1 

percent = (score/questions)*100
print("You got " + str(percent) + "%" + " questions correct")