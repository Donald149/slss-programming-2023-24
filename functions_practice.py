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
# print_area_of_a_square(12)

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