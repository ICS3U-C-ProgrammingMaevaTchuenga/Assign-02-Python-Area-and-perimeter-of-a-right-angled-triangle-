#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
# Hello Ms Raffin This program is to calculate and
#  display the area and perimeter of a right angled triangle


def main():
    # get the input from the user
    base = int(input("enter the base of the right angled triangle (cm) "))
    height = int(input("enter the height of the right angled triangle (cm) "))
    hypothenuse = int(input("enter the hypothenuse of the right angled triangle (cm) "))

    # calculate the area and perimeter of a right angled triangle

    Area = base * height / 2
    Perimeter = base + height + hypothenuse

    # display the output to the user
    print("the area of the right angled triangle is {} cm²".format(Area))
    print("the perimeter of the right angled triangle is {} cm".format(Perimeter))


if __name__ == "__main__":
    main()
