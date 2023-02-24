# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 09:01:09 2022

@author: Andrew
Description: This program allows for multiple options to be chosen through a menu.
 These options offer different experiences for the user.
"""

import os
import datetime
import math
import string
import secrets



#Password Generator
def pass_gen():
    """
    Generate a completely random password.

    Returns
    -------
    None.

    """
    print("PASSWORD GENERATOR")
    alphabet = string.ascii_letters + string.digits #Set valid characters to be letters and numbers.

    while True: #Generate an 8 character alphanumeric password with atleast one lowercase
    #and one uppercase characters and atleast 3 digits.
        password = ''.join(secrets.choice(alphabet) for i in range(10)) #Form new password.
        if (any(c.islower() for c in password) #check for lowercase letters.
            and any(c.isupper() for c in password) #check for uppercase letters.
            and sum(c.isdigit() for c in password) >= 3): #check for digits and amount of digits.
            break
    print("Your new password is: ", password)


#Percentage Math
def percent_math(numerator, denominator):
    """

    Parameters
    ----------
    numerator : INT
        Top number of fraction
    denominator : INT
        Bottom number of fraction

    Returns
    -------
    None.

    """

    numerator = int(numerator)
    denominator = int(denominator)
    print("PERCENTAGE MATH")
    while denominator == 0:
        print("ERROR! Cannot divide by zero. Try again")
        denominator = input("Enter a value for the denominator: ")
        denominator = int(denominator)

    percentage = round((numerator / denominator) * 100, 2) #Round the devision to 2 decimal places

    print(numerator,"/", denominator,"is approximately equal to", percentage,"%")

#Day Calculator
def day_calc():
    """
    Calculate the number of days from today until July 4, 2025.

    Returns
    -------
    None.

    """
    print("DAY CALCULATOR\n")
    target_date = datetime.date(2025, 7, 4)
    today_date = datetime.date.today()#Get today's date
    delta = target_date - today_date

    print("There are", delta,"remaining till", target_date)
    input("\nPress ENTER to continue")

#Triangle Calculation using Law of Cosines
def triangle_math(leg_a, leg_b, angle_ab):
    """


    Parameters
    ----------
    leg_a : INT
        Side 'a' of a triangle.
    leg_b : INT
        Side 'b' of a triangle.
    angle_ab : INT
        Angle C of a triangle. (0 < x < 180)

    Returns
    -------
    None.

    """
    leg_a = int(leg_a)
    leg_b = int(leg_b)
    angle_ab = int(angle_ab)

    try:
        print("TRIANGLE MATH")
        while leg_a <= 0 or leg_b <= 0:
            print("ERROR: Both sides must be greater than 0!")
            if leg_a <= 0:
                leg_a = input("Enter a valid value for leg_a: ")
            if leg_b <= 0:
                leg_b = input("Enter a valid value for leg_b: ")
    except ValueError:
        pass

    while angle_ab >= 180 or angle_ab <= 0:
        print("ERROR: Angle must be between 1 and 179")
        angle_ab = input("Enter a value for the angle in degrees: ")
        angle_ab = int(angle_ab)

    angle_ab = math.radians(angle_ab) #Format angle_ab into radians for accurate measurement.
    angle_cos = math.cos(angle_ab) #Find the cosine of angle_ab.
    leg_c = math.sqrt((leg_a ** 2) +
                      (leg_b ** 2) - (2 * leg_a * leg_b * angle_cos))
    #sqrt(a^2 + b^2 - (2*a*b*cos(angle_ab))).

    print("Leg C is equal to:", leg_c,"units")

#Volume Calculation
def volume_calc(height, radius):
    """

    Parameters
    ----------
    height : INT
        Height of cylinder.
    radius : INT
        Radius of cylinder base.

    Returns
    -------
    None.

    """

    height = int(height)
    radius = int(radius)

    print("VOLUME CALCULATOR")

    while height <= 0 or radius <= 0:
        try:
            print("ERROR: Height nor Radius cant be zero or negative! Try Again")
            if height <= 0:
                height = input("Enter value for height: ")
            if radius <= 0:
                radius = input("Enter value for radius: ")
        except ValueError:
            pass

    volume = math.pi * (radius ** 2) * height #v=pi*r^2*h.

    print("The volume of the cylinder is:", volume,"units^3")

#Menu
def menu():
    """
    Display the menu.

    Returns
    -------
    None.

    """
    print("a. Generate Secure Password")
    print("b. Calculate and Format a Percentage")
    print("c. How many days from today until July 4, 2025?")
    print("d. Use the Law of Cosines to calculate the leg of a triangle.")
    print("e. Calculate the volume of a Right Circular Cylinder")
    print("f. Exit program")

def rtm():
    """

    Returns
    -------
    None.

    """
    input("\nPress ENTER to return to Menu.\n")

#MAIN
def main():
    """
    Call the menu and then call the appropriate menu option according to
    selection and run accordinglly.

    Returns
    -------
    None.

    """

    while True:
        menu()
        menu_selection = input("\nInput a corresponding letter to access menu option: ")
        menu_selection = menu_selection.lower()


        if menu_selection == "a": #Password Generator
            pass_gen()
            rtm()

        elif menu_selection == "b": #Percentage Calculator
            try:
                numerator = input("Enter value for the numerator: ")
                denominator = input("Enter value for the denominator: ")
            except ValueError:
                pass
            percent_math(numerator, denominator)
            rtm()

        elif menu_selection == "c": #Date Calculator
            day_calc()
            rtm()

        elif menu_selection == "d": #Triangle Math
            try:
                leg_a = input("Enter the length of side a: ")
                leg_b = input("Enter the length of side b: ")
                angle_ab = input("Enter the angle (in decimal form) inbetween side a and b: ")
            except ValueError:
                pass
            triangle_math(leg_a, leg_b, angle_ab)
            rtm()

        elif menu_selection == "e": #Volume of Cylinder
            try:
                height = input("Enter the height of a cylinder: ")
                radius = input("Enter the radius of a cylinder: ")
            except ValueError:
                pass
            volume_calc(height, radius)
            rtm()

        elif menu_selection == "f": #EXIT
            input("Press ENTER to exit the program.")
            break #End of program

        else: #Invalid input error check
            os.system('cls') #Clear the consol
            print("INVALID INPUT! Please try again.\n")


main()#Call main to properly run the program
