#!/usr/bin/env python3
"""
wardrobe_1.py
This program uses a Clothing class to keep track of my wardrobe.
@author Tset Noitamotua
@version 2017-05-03
"""


class Clothing(object):
    """
    The Clothing class defines a piece of clothing in terms of
    its name its cleanliness.
    """
    # constructor - instance variables
    def __init__(self, name, clean=True, times_worn=0, max_wear=1):
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wear = max_wear

    # getter & setter methods
    def get_name(self):
        return self.name
    def is_clean(self):
        return self.clean

    # other methods
    def wear(self):
        self.times_worn += 1
        if self.times_worn >= self.max_wear:
            self.clean = False
    def wash(self):
        self.clean = True
        self.times_worn = 0

    def __str__(self):
        return "Clothing[name=" + self.name + \
               ", clean="       + str(self.clean) + \
               ", times_word="  + str(self.times_worn) + \
               ", max_wear="    + str(self.max_wear) + \
               "]"


def main():
    # test the Clothing class
    myJeans = Clothing("blue jeans", False)
    print(myJeans)
    myJeans2 = Clothing("black jeans", clean=True)
    print(myJeans2)
    myJeans.wear()
    print(myJeans)
    myJeans.wash()
    print(myJeans)

if __name__ == "__main__":
    main()
