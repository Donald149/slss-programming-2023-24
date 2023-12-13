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

    if (g > 120 and r < 80 and b < 80) or (r < g and b < g):
        return "green"