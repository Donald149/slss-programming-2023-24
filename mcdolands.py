# McDoland's
# Author: Donald
# 1 November 2023

# Greets the user
print("Hello, this is McDoland's.")

# Ask for burger and fries
burger_choice = input("Would you like a burger for $5? (Yes/No) ").strip(",.?! ").lower()
fries_choice = input("Would you like fries for $3? (Yes/No) ").strip(",.?! ").lower()

# Math
total_bill = 0

if(burger_choice == "yes"):
    total_bill += 5

if(fries_choice == "yes"):
    total_bill += 3

tax = 0.14

total_bill = total_bill + total_bill * tax

# Response
if(total_bill > 0):
    print(f"Your total is {total_bill:.2f}")
else:
    print("GET OUTTA HERE IF YOU AINT ORDERING!!!")