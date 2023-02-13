print("This is a quiz game")

score = 0

question1 = input("Who wrote this programme:")
answer1= "emmanuel seun"
if answer1 == question1:
    score = score+1
else:
    score = score - 1
print(f"you scored: {score}")

question2 = input("A plane chrashed in between the boarder of U.S and canada.Where will they burry the survival?:")
answer2= "survivals are still alive"
if answer2 == question2:
    score= score+1
else:
    score = score - 1
print(f"you scored: {score}")

question3 = input("A square is_____side:")
answer3="4"
if answer3 == question3:
    score = score+1
else:
    score = score - 1
print(f"you scored: {score}")

question4 = input("At what year did Nigeria gain independence:")
answer4="1960"
if answer4 == question4:
    score = score+1
else:
    score = score-1
print(f"you scored: {score}")
question5 = input("Guess a number from 0-10:")
answer5="4"
if answer5 == question5:
    score = score+1
else:
    score = score-1
print(f"you scored: {score}")
