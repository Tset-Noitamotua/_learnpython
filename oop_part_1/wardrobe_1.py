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
    def __init__(self, name, clean=True):
        self.name = name
        self.clean = clean
    # getter & setter methods
    def get_name(self):
        return self.name
    def is_clean(self):
        return self.clean

    def __str__(self):
        return "Name: {} \
        \nCleanliness: {}".format(self.name, self.clean)


def main():
    # test the Clothing class
    myJeans = Clothing("blue jeans", False)
    myShorts = Clothing("shorts")
    print(myJeans.get_name())
    print(myJeans.is_clean())
    print(myShorts.is_clean())
    print(myShorts.get_name())
    print(myJeans)
    print(myShorts)




if __name__ == "__main__":
    main()
