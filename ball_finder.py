# Red Ball Finder 
# AUthor: Donald
# 12 January 2024

# Find red ball

from PIL import Image

import colour_helper

with Image.open("./Images/Red Ball.jpeg") as im:
    h = im.height
    w = im.width

    red_pixel = []
    x_value = 0
    y_value = 0

    for y in range(h):
        for x in range(w):
            current_pixel = im.getpixel((x, y))

            if colour_helper.pixel_to_string(current_pixel) == "red":
                red_pixel.append((x, y))
                x_value += x
                y_value += y
            
    average_x = round(x_value / len(red_pixel))
    average_y = round(y_value / len(red_pixel))

print(f"The center of the ball is at ({average_x}, {average_y})")
