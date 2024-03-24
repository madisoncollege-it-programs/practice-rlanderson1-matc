#!/usr/bin/env python3

#Author:  Rae Denruiter
#User input for temperature in Fahrenheit and convert it to Celsius.

#Import the f2c script

import f2c
def main():
    #Asking the user to imput a temperature

    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    #Calling the function with the user imput

    result = f2c.convert_temp(degrees_fahrenheit)
    
    #Print the result
    print("Temperature in Celsios:", result)

if __name__ == "__main__":
    main()