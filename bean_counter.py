# Jelly Bean Colour Counter
# Author: Donald
# 9 January 2024

# Version 01
# Count all red pixels
# Report on the red percentage
# Version 02 
# Counts the green pixels and reports %
# Version 03
# Recognise more colours 


from PIL import Image

import colour_helper

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []
blue_pixels = []
white_pixels = []
total_pixels = 0

img_width = jelly_bean_img.width
img_height = jelly_bean_img.height
total_pixels = img_width * img_height

# visit every pixel in the image
for y in range(img_height):
    for x in range(img_width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        # if that pixel is red, store the location(?)
        if colour_helper.pixel_to_string(current_pixel) == "white":
            white_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "green":
            green_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "blue":
            blue_pixels.append((x, y))
        else:
            jelly_bean_img.putpixel((x, y), (0, 0, 0))

jelly_bean_img.save("./Images/coloured_beans_test.jpg")

red_pixel_map = Image.new("RGB", (img_width, img_height))
for location in red_pixels:
    red_pixel_map.putpixel(location, colour_helper.RED_PIXEL)

red_pixel_map.save("./Images/red_pixelmap.jpg")
red_pixel_map.close()

green_pixel_map = Image.new("RGB", (img_width, img_height))
for location in green_pixels:
    green_pixel_map.putpixel(location, colour_helper.GREEN_PIXEL)

green_pixel_map.save("./Images/green_pixelmap.jpg")
green_pixel_map.close()

blue_pixel_map = Image.new("RGB", (img_width, img_height))
for location in blue_pixels:
    blue_pixel_map.putpixel(location, colour_helper.BLUE_PIXEL)

blue_pixel_map.save("./Images/blue_pixelmap.jpg")
blue_pixel_map.close()

# Count every pixel in the list
# get the percent
red_percent = round(len(red_pixels) / total_pixels * 100, 2)
green_percent = round(len(green_pixels) / total_pixels * 100, 2)
blue_percent = round(len(blue_pixels)/ total_pixels * 100, 2)

print(f"There is {red_percent}% of red beans.")
print(f"There is {green_percent}% of green beans.")
print(f"There is {blue_percent}% of blue beans.")

jelly_bean_img.close()