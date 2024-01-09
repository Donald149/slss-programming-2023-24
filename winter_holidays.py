# Winter Holidays
# Author: Donald
# 8 January 2024

# Requirements:
#    - creates a function that takes one param
#    - returns a summary of an event from your holidays

import random 

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - string that indicates whether the event
            is good or bad

    Returns:
        an event that happened to you during the holidays 
        the event is selected part
    """
    good = ["I ate some good food.",
            "I watched a movie with my friends.",
            "I beat a difficult video game boss.",
            "I read a really good manga."]

    bad = ["There was no snow during Christmas.",
           "Some stupid people threw my shoe up a roof.",
           "I spent too much time on my phone."]

    if good_or_bad.lower() == "good":
        return random.choice(good)
    elif good_or_bad.lower() == "bad":
        return random.choice(bad)
    else:
        return "Hmm..."


def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday(input("Do you want to hear a good or bad event? ")))

# If we're running THIS FILE using Python
if __name__ == "__main__":
    main()