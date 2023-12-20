# Images and Python
# Author: Donald
# 11 November 2023

import colour_helper

from PIL import Image


# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # algorithm to visit ebvery pixel in the kid-green image
    # store the height and width of the image
    image_height = im.height
    image_width = im.width

    # load background image
    bg_im = Image.open("./Images/beach.jpg")

    # outer loop is top -> bottom
    # inner loop is left -> right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            # check pixel if it's green
            if colour_helper.pixel_to_string(pixel) == "green":
                # replace with bg_pixel
                bg_pixel = bg_im.getpixel((x, y))
                im.putpixel((x, y), bg_pixel)
            
    bg_im.close()

    # save the image
    im.save("./Images/output.jpg")

with Image.open("./Images/best_pizza.jpg") as pic:
    # go through every pixel
    for y in range(pic.height):
        for x in range(pic.width):
            pixel = pic.getpixel((x, y))

            # check if light
            if colour_helper.is_light(pixel):
                # replace
                pic.putpixel((x,y), colour_helper.WHITE_PIXEL)
            else:
                pic.putpixel((x, y), colour_helper.BLACK_PIXEL)

    # save
    pic.save("./Images/output_pizza.jpg")

with Image.open("./Images/best_pizza.jpg") as pic_2:
    for y in range(pic_2.height):
        for x in range(pic_2.width):
            pixel = pic_2.getpixel((x, y))

            pic_2.putpixel((x,y), colour_helper.pixel_to_grayscale(pixel))

    # save
    pic_2.save("./Images/output2_pizza.jpg")