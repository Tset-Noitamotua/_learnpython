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
    def __init__(self, name, clean=True, time_worn=0, max_wear=1):
        self.name = name
        self.clean = clean
        self.times_worn = time_worn
        self.max_wear = max_wear

    # getter & setter methods
    def get_name(self):
        return self.name
    def is_clean(self):
        return self.clean
    def wear(self):
        self.times_worn += 1
        if self.times_worn >= self.max_wear:
            self.clean = False
    def wash(self):
        self.clean = True
        self.times_worn = 0

    def __str__(self):
        return "Name: {} \
        \nCleanliness: {}".format(self.name, self.clean)



def main():
    # test the Clothing class
    pass



if __name__ == "__main__":
    main()