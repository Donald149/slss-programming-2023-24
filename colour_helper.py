# Colour helper
# Author: Donald
# 13 December 2023

# Need help with colour?
# This shall help you!


def pixel_to_string(pixel:tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name
    
    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if (g > 120 and r < 150 and b < 150) or ((r + b) < g):
        return "green"
    

def is_light(pixel: tuple) -> bool:
    """Determines if a pixel is light or not. 
    Takes the pixel values and averages it.
    
    Params:
        pixel- 3-tuple of (red, green, blue)
        
    Return:
        True if average RGB value is greater than or equal to 128,  
        False if less than 128.
    """
    r, g, b = pixel

    average_value = (r + g + b) / 3

    if average_value >= 128:
        return True
    else:
        return False

black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128, 128, 128)
white_pixel = (255, 255, 255)


print(is_light(white_pixel))  # True
print(is_light(light_gray_pixel))  # True
print(is_light(dark_gray_pixel))  # False
print(is_light(black_pixel))  # False

def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Takes a pixel and return a grayscale version.
    
    Params:
        pixel- 3-tuple of (red, green, blue)
    
    Return:
    The grayscale
    """
    ave = int(sum(pixel) / len(pixel))
    return(ave, ave, ave)