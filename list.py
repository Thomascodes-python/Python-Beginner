tarred_road = ["jide", "john", "david", "ruth", "ojike", "seun", "wisdom", "jude", "kelvin", 12]

for house in tarred_road:
    if house == "seun":
        print("Seun is there")
        break
    else:
        print("Seun is not found")

street = ['house1', 'house2', 'house3']
street_ans = [20, 30, 40]
score = 0

for house_num in range(len(street)):
    user_input = int(input(f"{street[house_num]}: "))

    if street_ans[house_num] == user_input:
        score = score + 1
    print(f"Score: {score}")
