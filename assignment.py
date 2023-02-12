# users_name = input("what's your name:")

# if users_name == "Bond":
#     print("Welcome on board 007")
# else:
#     print(f"Good morning {users_name}")



house = 1000000

house_price_budget = int(input("What's your budget for this house:"))

if house_price_budget < 500000 and house_price_budget > 300000:
    downpayment = 10/100*house
    print(f"The downpayment is {downpayment} ")
elif house_price_budget > 500000:
    downpayment = 20/100*house
    print(f"The downpayment is {downpayment}")


