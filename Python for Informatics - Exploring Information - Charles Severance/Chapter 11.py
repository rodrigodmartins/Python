__author__ = 'rodri'

##Page 141

#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.rstrip()
#    if re.search('From:',line): print (line)
#
#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.rstrip()
#    x = re.findall('\S+@\S+',line)
#    if len(x) >0: print(x)
#
#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.rstrip()
#    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
#    if len(x) >0: print(x)
#
#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.strip()
#    if re.search('^X-\S*: [0-9.]+', line): print (line)
#
#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.strip()
#    x = re.findall('^X-\S*: ([0-9.]+)', line)
#    if len(x) >0: print(x)
#
#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.strip()
#    x = re.findall('^Details:.*rev=([0-9]+)', line)
#    if len(x) >0: print(x)
#
#import re
#file = open('mbox-short.txt')
#for line in file:
#    line = line.strip()
#    x = re.findall('^From .*([0-9][0-9]):', line)
#    if len(x) >0: print(x)

##Exercise 11.1 (page 152)
# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular
# expression and count the number of lines that matched the regular expression:

#import re
#expr = input('Enter a regular expression: ')
#file = open('mbox.txt')
#count = 0
#for line in file:
#    if re.findall(expr, line):
#        count += 1
#print ('mbox.txt had',count,'lines that matched',expr)

##Exercise 11.2
# Write a program to look for lines of the form
#
# New Revision: 39772
#
# and extract the number from each of the lines using a regular expression and the findall() method. Compute the
# average of the numbers and print out the average.

import re
file = input('Enter file: ')
try:
    lines = open(file)
except:
    print('Error reading file')
summ = 0
count = 0
for line in lines:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        #y = [int(i) for i in x]
        print(x)
        #print(type(y))
        #summ = summ + y
        #count = count + 1
print(sum(summ))
print(count)
#print ('Average:',sum/count)