# Loop Practice
# Author: Donald
# Date: 10 October 2023

# Create a list of groceries
groceries = ["ice cream", "juice", "bread", "waffles"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#    * ice cream
#      ---
#    * juice
#      ---
#      etc.

# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[2]}")
# print(f"  ---")

for item in groceries:
    print(f"* {item}")
    print(f"  ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

stars = ["*", "**", "***", "****", "*****", "******"]

for row in stars:
    print(row)

# Problem:
# Create a New Years Countddown that's automated
# Requirements:
#   - starts at 10
#   - counts down every second printing the second it's at
#   - instead of reaching zero, it prints out "Happy New Year"

import time

# Method 1

# countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
# for number in countdown:
#     print(number)
#     time.sleep(1)
# print("Happy New Year!")

# Method 2 (I made this up)
for i in range(10):
    down = 10 - i
    print(down)
    time.sleep(1)
print("Happy New Year!")

# Implement Linear Search
names = ['Anthony Maldonado', 'Randy Love', 'Christopher Valdez', 'Rodney Odom', 'Kimberly Ramos', 'Lisa Ray', 'Kevin Terry', 'Gregory Romero', 'Debbie Harris', 'Edwin Hall', 'Mark Myers', 'Lisa Long', 'Stephanie Watson', 'Katherine Fields', 'Kathryn Olson', 'Maurice Baxter', 'Russell Caldwell', 'Heather Griffin', 'Kara Lane', 'Mark Tucker', 'Kathryn Rodriguez', 'Rachael Daniels', 'Debra Whitaker', 'Angela Neal', 'Michelle Hall', 'Jessica Olson', 'Lynn Jensen', 'Marc Ray', 'Valerie Harris', 'Tina Webb', 'Donna Green', 'Derek Mcgee', 'Tammy Hall DVM', 'Christopher Johnston', 'Eric Smith', 'Matthew Lopez', 'Mary Smith', 'Dr. Heather Ramos MD', 'Eric Johnson', 'Dylan Alvarado', 'Aaron Huff', 'Robin James', 'Sandra Stevens', 'Scott Thomas', 'Philip Nelson', 'Marcus Martin', 'Mary Alexander', 'Jason James', 'Samantha Burch', 'Jessica Martinez', 'Jose Wright', 'Zachary Pineda', 'William Ramos', 'Shelby Hughes', 'Melanie Moore', 'Kimberly Fowler', 'Jordan Jones', 'Brenda Anderson', 'Russell Coleman', 'Jeremy Snow', 'Billy Wu', 'Jesse Rodriguez', 'Andrew Shea', 'Jason Castillo', 'Donald Abbott', 'Richard Cervantes Jr.', 'Jeffrey Powell', 'Angel Fernandez', 'Michelle Donovan', 'Mr. Michael Wagner DDS', 'Kimberly Gonzalez', 'Thomas Smith', 'Nichole Barnes', 'Shelly Clark', 'Ashley Ortiz', 'Jessica Lam', 'Kimberly Ray MD', 'Mason Kennedy', 'Whitney Harrington', 'Nicole Tran', 'Robert Montgomery', 'Ryan Gardner', 'Kimberly Silva', 'Stephanie Rivera', 'William Santos', 'Ashley Mcclain', 'Sophia Williams', 'Kevin Herring', 'Tyrone Leonard', 'Carolyn Jones', 'Stephanie Willis', 'Jon Lang', 'Tammy Porter', 'Robert Garcia', 'Casey Brown', 'Benjamin Aguilar', 'Nancy Norman', 'Aaron Peters', 'Blake Graham', 'Noah Harper DDS', 'Dwayne Ortiz', 'Melissa Padilla', 'Rebecca Jones', 'Michael Wood', 'Daniel Bean', 'Alexander Kaufman', 'Michael Higgins', 'Richard Bailey', 'Jay Cisneros', 'Lisa Acevedo', 'Sarah Hernandez', 'Bryan Jones', 'Mark Kennedy', 'Robert Caldwell', 'Larry Wolf', 'Robert Adkins', 'Wanda Doyle', 'Thomas Brown', 'Kevin Key', 'Stacey Fisher', 'Amber Hart', 'Paul Russell', 'Jacqueline David', 'Shannon Parker', 'Lisa Sanchez', 'Jennifer Atkins', 'Jason Woods', 'Richard Garcia', 'Luis Williams', 'Marco Weaver', 'Amy Hayes', 'Elizabeth Doyle DDS', 'Nicole Smith', 'Karen Thomas', 'Randy Reese', 'Deanna Rodriguez', 'Christian Conway', 'Craig Doyle', 'Dennis Oneill', 'Diane Jordan', 'Patrick Holder', 'Christina Thompson', 'Deanna Lee', 'Kathleen Davis', 'Brian Cox', 'Kristen Thomas', 'Samantha Smith', 'William Moss', 'Matthew Flowers', 'Megan Powell', 'Richard Williamson', 'Cindy Glenn', 'John Taylor', 'Nathaniel Lee', 'Sara Glover', 'James Jackson II', 'Carlos Henderson', 'Edward Holder', 'Whitney Hansen', 'Matthew Jacobs', 'Raymond Rodriguez', 'Christy Kennedy', 'Lisa Johnson', 'Mark Harris', 'Stephen Bowers', 'Derrick Brown', 'Stephen Schroeder', 'Martin Lawrence', 'Brian Reed', 'Trevor Booker', 'Ruben Johnson', 'Jeffrey Griffith', 'William Townsend', 'Cynthia Park', 'Carla Yang', 'Oscar Hartman', 'Shawn Hendricks', 'Timothy Oconnor', 'Gina Robertson', 'Jennifer Rodriguez', 'Jared Harris', 'Austin Austin', 'Nathan Golden', 'Samantha Flores', 'Alexis Jones', 'Susan Rice', 'Randall Holmes', 'Connie Johnson', 'Carol Young', 'Brandon Norris', 'Timothy Lester', 'Dustin Mccarthy', 'Tammy Brock', 'Heather Cummings', 'John Moreno', 'Dawn Berry', 'Jeffrey Montes', 'Joshua Smith', 'Alexa Barber', 'Mark Lewis']
search_name = "Joesph John"

for name in names:
    # Check if it's the name we want
    if name == search_name:
        print(f"We found {search_name}!!")
        
        break # STOPS THE LOOP
else:
    print(f"We didn't find {search_name}.")

# Print out something 20 times
for _ in range(20):
    print("The One Piece is REAL!!!")

# Repeat something 5 times and we want to keep track of how many iterations we've completed
for i in range(5):
	print(i)
     
for i in range(10):
    print(f"{i + 1}. You shall not pass.")