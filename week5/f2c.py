#!/usr/bin/env python3
#Author:  Rae Denruiter
#Description:  This script converts temperature from Fahrenheit to Celsius
def convert_temp(degrees_fahrenheit):

    """

    Convert Fahrenheit to Celsius

    Formula:
    (F - 32) x 5/9 = C

    """

    degrees_celsius = (degrees_fahrenheit - 32) * 5/9
    return degrees_celsius

def main():
    #Calling conver_temp function with an argument of 32
    result = convert_temp(32)
    print(result)

if __name__ == "__main__":
    main()