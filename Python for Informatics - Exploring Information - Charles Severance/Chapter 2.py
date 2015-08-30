__author__ = 'Rodrigo'

##Date: 06/June/2015
##Python 3.4.3 / Anaconda 2.2.0 (64-bit) / PyCharm Community Edition 4.5

## Exercise 2.1
#Type the following statements in the Python interpreter to see what they do:

5       #Nothing in the script, '5' in the console.
x = 5   #Nothing (both)
x + 1   #Nothing in the script, '6' in the console.

## Exercise 2.2
#Write a program that uses raw_input to prompt a user for their name and then welcomes them.

name = input('What is your name?\n')
print('Hello',name)

## Exercise 2.3
#Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = float(input('Please input number of hours: '))
rate = float(input('Please input rate per hour: '))
print('You have to pay:',(hours*rate))

## Exercise 2.4
#Assume that we execute the following assignment statements:
#
#width = 17
#height = 12.0
#
#For each of the following expressions, write the value of the expression and the type (of the value of the expression).
#
#1. width/2
#2. width/2.0
#3. height/3
#4. 1 + 2 * 5

width = 17
height = 12.0

print(type(width/2))    #<class 'float'>
print(type(width/2.0))  #<class 'float'>
print(type(height/3))   #<class 'float'>
print(type(1 + 2 * 5))  #<class 'int'>

## Exercise 2.5
#Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

#TF = (9/5)TC + 32

tc = float(input('Please input temperature in degrees Celsius: '))
tf = float((9/5*tc)+32)
print('The temperature in degrees Farenheit is:',tf)
