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

    # GO through every pixel and add their value to a variable if red
    for y in range(h):
        for x in range(w):
            current_pixel = im.getpixel((x, y))

            pixel_result = colour_helper.pixel_to_string(current_pixel)

            if pixel_result == "red" or pixel_result == "ball red":
                red_pixel.append((x, y))
                x_value += x
                y_value += y
            
    # Average value to determine the "center"         
    average_x = round(x_value / len(red_pixel))
    average_y = round(y_value / len(red_pixel))

    # Creating a pixel map for accuracy check
    red_pixel_map = Image.new("RGB", (w, h))

    for y in range(h):
        for x in range(w):
            if (x ,y) in red_pixel:
                red_pixel_map.putpixel((x ,y), colour_helper.RED_PIXEL)
            else:
                red_pixel_map.putpixel((x, y), colour_helper.BLACK_PIXEL)
                
    red_pixel_map.save("./Images/red_pixelmap.jpg")
    red_pixel_map.close()

# Result output
print(f"The center of the ball is at ({average_x}, {average_y})")