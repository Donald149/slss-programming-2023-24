# Functions Practice
# Author: Donald 
# 24 November 2023

def area_of_a_square(sidelength: float) -> float:
	"""Return the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square
	"""

	area = sidelength ** 2

	return area



def print_area_of_a_square(sidelength: float):
	"""Calculate and print the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square
	"""
	
	area = sidelength ** 2
	
	print(f"The area of a square with sidelength {sidelength} is: {area} square units.")



print_area_of_a_square(12.2)
print_area_of_a_square(12)

# Given two squares of two sidelengths
#   12.2 and 144
# Add the area of both squares

area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
print(area_of_squares)

# Question 1:
# Create a function called stars()
# Takes an int as a parameter
# Returns a string of stars of given length

# Aside: Signature of a function
# 	- name of the function
# 	- inputs/parameters /type

def stars(star_amt: int) -> str:
	"""Prints an amount of stars.
	
	Params:
	
	star_amt - amount of stars
	"""
		
	return "*" * star_amt

star_input = int(input("How many stars? "))
print(stars(star_input))

# Question 2:
# Create a function called biggest_of_three()
# Takes three numbers and returns the biggest one

def biggest_of_three(num1: float, num2: float, num3: float) -> float:
	"""Takes three numbers.
	Returns the biggest of the three numbers.

	Params:

	num1 - 1st number,
	num2 - 2nd number,
	num3 - 3rd number,

	Returns:
	The biggest of the three numbers.
	"""

	biggest_num = 0
	number_list = [num1, num2, num3]

	for number in number_list:
		if number > biggest_num:
			biggest_num = number

	return biggest_num

print(biggest_of_three(10, 100, 1000))

# Question 3
# Question 4
# Create functions called pyramid() and pyramid_mirror()
# Takes one number as the parameter
# Creates a pyramid of that many layers

def pyramid(layers: int):
	"""Creates a pyramid of stars.
	
	Params:

	layers - how many layer of stars in the pyramid
	"""

	for level in range(layers):
		print(stars(level + 1))

pyramid_input = int(input("Enter amount of levels for the pyramid: "))
pyramid(pyramid_input)

def pyramid_mirror(layers: int):
	""" Creates a pyramid of stars, but mirrored.

	Params:

	layers - how many layers of stars in the pyramid
	"""

	for level in range(layers):
		reverse_space= " " * (layers - level - 1) 
		print(f"{reverse_space}{stars(level + 1)}")

mirror_input = int(input("Enter amount of levels for the mirror pyramid: "))
pyramid_mirror(mirror_input)