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



def stars(star_amt: int) -> str:
	"""Prints an amount of stars.
	
	Params:
	
	stars - amount of stars
	"""
	
	string = ""
	for _ in range(star_amt):
		string += "*"
		
	return string

star_input = int(input("How many stars? "))
print(stars(star_input))

def biggest_of_three(num1: int, num2: int, num3: int) -> int:
	"""Takes three numbers.
	Returns the biggest of the three numbers.

	Params:

	num1 - 1st number,
	num2 - 2nd number,
	num3 - 3rd number,
	"""

	biggest_num = 0
	number_list = [num1, num2, num3]

	for number in number_list:
		if number > biggest_num:
			biggest_num = number

	return biggest_num

print("Insert three numbers:")
input_num1 = int(input("1st number: "))
input_num2 = int(input("2nd number: "))
input_num3 = int(input("3rd number: "))
print(f"The biggest number is {biggest_of_three(input_num1, input_num2, input_num3)}.")

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

	mirror_layers - how many layers of stars in the pyramid
	"""

	for level in range(layers):
		reverse_space= " " * (layers - level - 1) 
		print(f"{reverse_space}{stars(level + 1)}")

mirror_input = int(input("Enter amount of levels for the mirror pyramid: "))
pyramid_mirror(mirror_input)