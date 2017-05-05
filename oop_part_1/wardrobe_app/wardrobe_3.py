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

class Shirt(Clothing):
    """
    The Shirt class inherits from Clothing class. Thus Clothing is a Superclass
    of the Shirt class.
    """
    # constructor
    def __init__(self, name, clean=True, times_worn=0, max_wear=1, shortsleeves=True):
        # initialize with same instance variables as the Clothing class
        super().__init__(name, clean, times_worn, max_wear)
        self.shortsleeves = shortsleeves
    def hasShortsleeves(self):
        return self.shortsleeves

    def __str__(self):
        return "Shirt[" + super().__str__() + \
               ", shortsleeves=" + str(self.shortsleeves) + \
               "]"



def main():
    # test the Clothing class
    myClothes = []
    myClothes.append(Clothing("blue jeans", False))
    myClothes.append(Clothing("baseball cap", True, 20, 1000))
    myClothes.append(Clothing("jacket", True, 20, 100))
    myClothes.append(Shirt("t-shirt", True, 0, 1, True))
    myClothes.append(Shirt("dress shirt", True, 0, 1, False))

    print("\n==== Full wardrobe =========")
    for i in range(len(myClothes)):
        print(myClothes[i])

    print("\n==== Clean clothes =========")
    for i in range(len(myClothes)):
        if myClothes[i].is_clean():
            print(myClothes[i])

    print("\n==== Dirty clothes =========")
    for i in range(len(myClothes)):
        if not myClothes[i].is_clean():
            print(myClothes[i])

    print("\n==== Shirts ================")
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            print(myClothes[i])

    print("\n==== Dirty Shirts ==========")
    # both shirts above are clean, thus we need to wear one of them
    # to have a dirty one.
    myClothes[4].wear()     # this is the second shirt in myClothes list
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            if not myClothes[i].is_clean():
                print(myClothes[i])


if __name__ == "__main__":
    main()
