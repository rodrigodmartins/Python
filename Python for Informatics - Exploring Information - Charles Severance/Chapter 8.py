__author__ = 'Rodrigo'

##Exercise 8.1
# Write a function called chop that takes a list and modifies it, removing the first and last elements, and
# returns None. Then write a function called middle that takes a list and returns a new list that contains all but
# the first and last elements.

lst = [1,2,3,4,5,6,7,8,9,10]

def chop():
    length = len(lst)
    #print (length)
    del (lst[length-1])
    del (lst[length-length])
    print (lst)
chop()

lst2 = [1,2,3,4,5,6,7,8,9,10]

def middle():
    length2 = len(lst2)
    #print (length)
    print (lst2[(length2-length2+1):(length2-1)])
middle()
print(lst2)

## Exercise 8.2
# Figure out which line of the above program is still not properly guarded. See if you can construct a text file which
# causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure
# it handles your new text file.

fhand = open('mbox-short.txt')
count = 0
days = []
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    days.append(words[2])
    print(days)

## Exercise 8.3
# Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression
# using the and logical operator with a single if statement.

fhand = open('mbox-short.txt')
count = 0
days = []
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    days.append(words[2])
    print(days)

## Exercise 8.4
# Download a copy of the file from www.py4inf.com/code/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words
# using the split function. For each word, check to see if the word is already in a list. If the word is not in the list,
# add it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill',
# 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

file = open('romeo.txt')
words = list()
for line in file:
    parts = line.split()
    if len(parts) == 0: continue
    for part in parts:
        if part not in words:
            words.append(part)
words.sort()
print(words)

##Exercise 8.5

file = open('mbox-short.txt')
lines = list()
for line in file:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    print (words[1])
    lines.append(words[1])
print('There were', len(lines),'lines in the file with From as the first word')

##Exercise 8.6

list = []
while True:
    value = input('Enter a number: ')
    if value == 'done':
       break
    try:
        value = float(value)
        list.append(value)
    except:
        print('Please enter a number')
if len(list) != 0 :
    print('Maximum :',max(list))
    print('Minimum :',min(list))
else: print('No values to calculate')