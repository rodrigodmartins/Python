__author__ = 'Rodrigo'

##Item 10.2
#txt = 'but soft what light in yonder window breaks'
#print (txt)
#print(type (txt))
#words = txt.split()
#print (words)
#print(type (words))
#t = list()
#for word in words:
#    t.append((len(word), word))
#
#print (t)
#print(type (t))
#t.sort(reverse=True)
#print (t)
#print(type (t))
#
#res = list()
#for length, word in t:
#    res.append(word)
#
#print (res)
#print(type (res))


##Item 10.6
#import string
#fhand = open ('romeo-full.txt')
#counts = dict()
#for line in fhand:
#    #line = line.translate(None,string.punctuation)
#    line = line.lower()
#    words = line.split()
#    for word in words:
#        if word not in counts:
#            counts[word] = 1
#        else:
#            counts[word] += 1
#print (counts)
#print(type(counts))
#
#Sort the dictionary by value
#lst = list()
#for key, val in counts.items():
#    lst.append((val, key))
#
#print(lst)
#print(type(lst))
#lst.sort(reverse=True)
#print(lst)
#print(type(lst))
#
#for key, val in lst[:10]:
#    print (key,':', val)


##Exercise 10.1
# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary. After all the data has been read, print the person
# with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse
# order and print out the person who has the most commits.
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
#
#file = input('Please input file name: ')
#try:
#    lines = open(file)
#except:
#    print ('File could not be located. Terminating now.')
#    exit()
#
#dic = dict()
#for line in lines:
#    line = line.strip()
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    if words[1] not in dic :
#        dic[words[1]] = 1
#    else :
#        dic[words[1]] += 1
#
# Sorting dict by value
#lst = list()
#for key, val in dic.items():
#    lst.append((val, key))
#lst.sort(reverse=True)
#print (lst[0])
#for key, val in lst[:1]:
#    print (val,key)

##Exercise 10.2
# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the
# “From” line by finding the time string and then splitting that string into parts using the colon character. Once you
# have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
#
#Sample Execution:
#python timeofday.py
#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

##Option #1
#file = input('Please input file name: ')
#try:
#    lines = open(file)
#except:
#    print ('File could not be located. Terminating now.')
#    exit()
#
#dic = dict()
#for line in lines:
#    line = line.strip()
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    if words[5][0:2] not in dic :
#        dic[words[5][0:2]] = 1
#    else :
#        dic[words[5][0:2]] += 1
#for key in sorted(dic):
#    print (key,':',dic[key])
#
##Option #2
#
#file = input('Please input file name: ')
#try:
#    lines = open(file)
#except:
#    print ('File could not be located. Terminating now.')
#    exit()
#
#times = list()
#for line in lines:
#    line = line.strip()
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    times.append(words[5])
##print (times)
#colonpos = list()
#for time in times:
#    pos = time.find(':')
#    colonpos.append(pos)
##print (colonpos)
#
#hours = list()
#for i in list(range(1,len(colonpos)+1)):
#    temp1 = times[i-1]
#    temp2 = colonpos[i-1]
#    temp3 = temp1[:temp2]
#    hours.append(temp3)
##print(hours)
#dic = dict()
#for hour in hours:
#    dic[hour] = dic.get(hour,0)+1
#for key in sorted(dic):
#    print (key,':',dic[key])

##Exercise 10.3
# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should
# convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits,
# punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how
# letter frequency varies between languages.
# Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

import string
file = input('Please input file name: ')
try:
    lines = open(file)
except:
    print ('File could not be located. Terminating now.')
    exit()
intab = string.digits+string.punctuation
outtab = str(' ')*len(intab)
dic = dict()
for line in lines:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        if len(words) == 0 : continue
        letters = tuple(word)
        for letter in letters:
            letter = letter.translate(letter.maketrans(intab,outtab))
            if letter == ' ':continue
            dic[letter] = dic.get(letter,0)+1

#Sorting by alphabetical order of keys
print('Sorted by alphabetical order of keys:')
for key in sorted(dic):
    print (key,':',dic[key])
print('')
#Sorting by decreasing order of frequency
print('Sorted by decreasing order of frequency:')
lst = list()
for key, val in dic.items():
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst:
    print (val,':',key)