# Functions and Turtle
# Author: Donald
# 28 November 2023

import turtle

burt = turtle.Turtle()

burt.color("lightblue")

def squared(num: float) -> float:
    """Takes a number and squares and returns it."""

    return num ** 2


def draw_square(side_length: int) -> None:
    """Draws a square of a given length."""
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)


def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree 
    with initial given height in pixels
    
    Params:

    level - number representing the levels of branches
    height - height of the main tree in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left
        burt.left(36)
        #   a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)
        
        # 3. Turn turtle right
        burt.right(36 * 2)
        #   a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 4. Return to beginning
        burt.left(36)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0]) # revert colour

def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree 
    with initial given height in pixels
    
    Params:

    level - number representing the levels of branches
    height - height of the main tree in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left
        burt.left(42)
        #   a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.6)
    
        # 3. Turn turtle middle
        burt.right(42)
        #   a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.6)

        # 4. Turn turtle right
        burt.right(42)
        #   a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.6)

        # 5. Return to beginning
        burt.left(42)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0]) # revert colour

# Set-up Burt to draw trees
burt.color("brown")
burt.setheading(90)
burt.width(4)
burt.speed(0)

draw_fancy_tree(4, 175)

turtle.done()