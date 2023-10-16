# Star Wars BOt
# Author: Donald
# Date: 16 October 2023

# Ask the user if they like red or capes
print("I will decide whether you are worthy of joining the dark side.")
like_red = input("Do you like the colour red? ")
like_capes = input("Do you like capes? ")

# Give response based on inputs
if like_red.lower() == "yes":
    print("I welcome you to the dark side.")
elif like_red.lower() == "no":
    if like_capes.lower() == "yes":
        print("The dark side is your chosen path.")
    else:
        print("You should probably not join the dark side.")
        print("Rethink your career paths carefully...")
else:
    print("You are not cool enough. You are not allowed to join the dark side.")
    print("Go join the light side or something...")