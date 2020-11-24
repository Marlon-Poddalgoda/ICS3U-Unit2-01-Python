#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program calculates the area and circumference of a circle
#     with a radius of 15mm

import math


def main():
    # this function calculates/prints the area & circumference of the circle
    
    print("If a circle has a radius of 15 mm:")
    print("")
    print("Then...")
    print("")
    print("Area is {} mm²".format(math.pi*15**2))
    print("Circumference is {} mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
