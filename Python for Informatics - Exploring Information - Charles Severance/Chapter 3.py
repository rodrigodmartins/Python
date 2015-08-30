__author__ = 'Rodrigo'

##Date: 08/June/2015
##Python 3.4.3 / Anaconda 2.2.0 (64-bit) / PyCharm Community Edition 4.5

## Celsius to Farenheit
#Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

#TF = (9/5)TC + 32

try:
    tc = float(input('Please input temperature in degrees Celsius: '))
    tf = float((9/5*tc)+32)
    print('The temperature in degrees Farenheit is:',tf)
except:
    print('Please input a number')

## Exercise 3.1
#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input('Please input number of hours: '))
rate = float(input('Please input rate per hour: '))
if hours <= 40:
    print('You have to pay:',(hours*rate))
else:
    print('You have to pay:',((40*rate)+((hours-40)*1.5*rate)))

## Exercise 3.2
#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
# by printing a message and exiting the program. The following shows two executions of the program:

hours = input('Please input number of hours: ')
try:
    hours2 = float(hours)
except:
    print('Error, please enter numeric input')
    exit()

rate = input('Please input rate per hour: ')
try:
    rate2 = float(rate)
except:
    print('Error, please enter numeric input')
    exit()

if hours2 <= 40:
    print('You have to pay:',(hours2*rate2))
else:
    print('You have to pay:',((40*rate2)+((hours2-40)*1.5*rate2)))

## Exercise 3.3
#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an
#  error message. If the score is between 0.0 and 1.0, print a grade using the following table:

score = input('Please enter numeric score between 0.0 and 1.0: ')
try:
    score2 = float(score)
except:
    print('I said NUMERIC !!!')
    exit()

if score2 >= 0.9 and score2 <= 1.0:
    print('Grade: A')
elif score2 >= 0.8 and score2 < 0.9:
    print('Grade: B')
elif score2 >= 0.7 and score2 < 0.8:
    print('Grade: C')
elif score2 >= 0.6 and score2 < 0.7:
    print('Grade: D')
elif score2 >= 0.0 and score2 < 0.6:
    print('Grade: F')
elif score2 < 0 or score2 > 1:
    print('What part of "...between 0.0 and 1.0 ..." you did not understand?')