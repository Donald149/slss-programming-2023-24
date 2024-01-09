# Jelly Bean Colour Counter
# Author: Donald
# 9 January 2024

# Version 01
# Count all red pixels
# Report on the red percentage

from PIL import Image

import colour_helper

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []

# visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        # if that pixel is red, store the location(?)
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))

# Count every pixel in the list
# get the percent
red_percent = len(red_pixels) / (jelly_bean_img.width * jelly_bean_img.height)
print(red_percent)