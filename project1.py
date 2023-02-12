print("This is a quiz game")

score = None
pass


question1 = input("Who wrote this programme:")
answer1= "emmanuel seun"

question2 = input("What is the meaning of CPU:")
answer2= "central processing unit"

question3 = input("What is the full meaning of RAM:")
answer3="Random access memory"

question4 = input("At what time did Nigeria gain independence:")
answer4="1960"

question5 = input("What is an integer:")
answer5="a number"

if answer1 == question1:
    score = 0+1
    print(score)
elif answer2 == question2:
    print(score)
    score= 1+1
    print(score)
elif answer3 == question3:
    score = 2+1
    print(score)
elif answer4 == question4:
    score = 3+1
    print(score)
elif answer5 == question5:
    score = 4+1
    print(score)
print(score)
