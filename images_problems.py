# Functions solve Images Problems
# Author: Donald 
# 20 December 2023

from PIL import Image

import colour_helper

def binarized(filename: str) -> None:
    with Image.open(filename) as im:
    # go through every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel((x, y))

                # check if light
                if colour_helper.is_light(pixel):
                # replace
                    im.putpixel((x,y), colour_helper.WHITE_PIXEL)
                else:
                    im.putpixel((x, y), colour_helper.BLACK_PIXEL)

    # save
    im.save("./Images/binarized.jpg")

binarized("./Images/beach.jpg")