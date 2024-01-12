# Jelly Bean Colour Counter
# Author: Donald
# 9 January 2024

# Version 01
# Count all red pixels
# Report on the red percentage
# Version 02 
# Counts the green pixels and reports %


from PIL import Image

import colour_helper

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []
yellow_pixels = []
total_pixels = 0

img_width = jelly_bean_img.width
img_height = jelly_bean_img.height
total_pixels = img_width * img_height

# visit every pixel in the image
for y in range(img_height):
    for x in range(img_width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        # if that pixel is red, store the location(?)
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "green":
            green_pixels.append((x, y))

# Count every pixel in the list
# get the percent
red_percent = round(len(red_pixels) / (total_pixels) *100, 2)
green_percent = round(len(green_pixels) / (total_pixels) *100, 2)

print(f"There is {red_percent}% of red beans.")
print(f"There is {green_percent}% of green beans.")

jelly_bean_img.close()