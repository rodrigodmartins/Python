__author__ = 'Rodrigo'

##Date: 08/June/2015
##Python 3.4.3 / Anaconda 2.2.0 (64-bit) / PyCharm Community Edition 4.5

##Exercise 4.1
#Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

#import random
#for i in range(10):
#    x = random.random()
#    print (x)

#import random
#print(random.randint(1,10))

#import random
#t = [1,2,3,4,5,6]
#print(random.choice(t))

#import math
#print(math)
#print(math.pi)

##Exercise 4.2
#Move the last line of this program to the top, so the function call appears before the definitions.
#Run the program and see what error message you get.

#Correct
#def print_lyrics():
#    print ("I'm a lumberjack, and I'm okay.")
#    print ('I sleep all night and I work all day.')
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
#repeat_lyrics()

#Changed as per exercise

#repeat_lyrics()
#def print_lyrics():
#    print ("I'm a lumberjack, and I'm okay.")
#    print ('I sleep all night and I work all day.')
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

##Exercise 4.3
#Move the function call back to the bottom and move the definition of print_lyrics after the definition
# of repeat_lyrics. What happens when you run this program?


#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
#def print_lyrics():
#    print ("I'm a lumberjack, and I'm okay.")
#    print ('I sleep all night and I work all day.')
#repeat_lyrics()

##Exercise 4.4
#What is the purpose of the ”def” keyword in Python?
# b) It indicates the start of a function

##Exercise 4.5
#What will the following Python program print out?

#def fred():
#    print ("Zap")
#def jane():
#    print ("ABC")

#print(jane())
#print(fred())
#print(jane())

#d) ABC Zap ABC

##Exercise 4.6
#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
# which takes two parameters (hours and rate).

#def computepay(hours,rate):
#    try:
#        hours2 = return(float(hours))
#    except:
#        print('Error, please enter numeric input')
#        exit()
#    try:
#        rate2 = return(float(rate))
#    except:
#        print('Error, please enter numeric input')
#        exit()
#    if hours2 <= 40:
#        return('You have to pay:',(hours2*rate2))
#    else:
#        return('You have to pay:',((40*rate2)+((hours2-40)*1.5*rate2)))

def computepay(hours,rate):
    if hours <= 40:
        print(hours,rate)
    else:
        print((40*rate2)+((hours2-40)*1.5*rate2))

