__author__ = 'Rodrigo'

##Exercise 9.1

#lines = open('words.txt')
#dic = dict()
#for line in lines:
#    line = line.strip()
#    line = line.lower()
#    words = line.split()
#    if len(words) == 0: continue
#    for word in words:
#        if word not in dic:
#            dic[word] = 1
#        else:
#            dic[word] += 1
#print (dic)
#
#print('rewarding' in dic)
#print('will' in dic)
#print('Will' in dic)
#
#print (dic.get('programs',0))
#print (dic.get('we',0))
#print (dic.get('that',0))


##Example page 111

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
#    #line = line.lower()
#    words = line.split()
#    if len(words) == 0: continue
#    for word in words:
#        dic[word] = dic.get(word,0)+1
#print (dic)
#
##Example page 112
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
#    line = line.lower()
#    words = line.split()
#    if len(words) == 0: continue
#    for word in words:
#        dic[word] = dic.get(word,0)+1
#for key in dic:
#    print (key,':',dic[key])

## Sorting

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
#    line = line.lower()
#    words = line.split()
#    if len(words) == 0: continue
#    for word in words:
#        dic[word] = dic.get(word,0)+1
#for key in sorted(dic):
#    print (key,':',dic[key])

## Deleting punctuation

#import string
#file = input('Please input file name: ')
#try:
#    lines = open(file)
#except:
#    print ('File could not be located. Terminating now.')
#    exit()
#
#dic = dict()
#for line in lines:
#    #line = line.translate(None, string.punctuation)
#    line = line.strip()
#   line = line.lower()
#    words = line.split()
#    if len(words) == 0: continue
#   for word in words:
#       dic[word] = dic.get(word,0)+1
#for key in sorted(dic):
#    print (key,':',dic[key])

##Exercise 9.2
# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that
# start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program
# print out the contents of your dictionary (order does not matter).
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
#    #line = line.lower()
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    #print(words[2])
#    if words[2] not in dic :
#        dic[words[2]] = 1
#    else :
#        dic[words[2]] += 1
#for key in sorted(dic):
#    print (key,':',dic[key])

##Exercise 9.3
# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

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
#    #line = line.lower()
#    words = line.split()
#    if len(words) == 0 or words[0] != 'From': continue
#    #print(words[2])
#    if words[1] not in dic :
#        dic[words[1]] = 1
#    else :
#        dic[words[1]] += 1
#for key in sorted(dic):
#    print (key,':',dic[key])

##Exercise 9.4
# Add code to the above program to figure out who has the most messages in the file. After all the data has been read and
# the dictionary has been created, look through the dictionary using a maximum loop (see Section 5.7.2) to find who has the
# most messages and print how many messages the person has.

file = input('Please input file name: ')
try:
    lines = open(file)
except:
    print ('File could not be located. Terminating now.')
    exit()

dic = dict()
for line in lines:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    if words[1] not in dic :
        dic[words[1]] = 1
    else :
        dic[words[1]] += 1
vals = dic.values()
largest = 0
for num in vals:
    if largest is None or num > largest:
        largest = num
for key in dic:
    if dic[key] == largest:
        print(key,':',largest)

##Exercise 9.5
# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

file = input('Please input file name: ')
try:
    lines = open(file)
except:
    print ('File could not be located. Terminating now.')
    exit()

emails = list()
for line in lines:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    emails.append(words[1])
atpos = list()
for email in emails:
    pos = email.find('@')
    atpos.append(pos)
#print(emails)
#print(atpos)
domains = list()
for i in list(range(1,len(atpos)+1)):
    temp = emails[i-1]
    #print (temp)
    temp2 = temp[atpos[i-1]+1:]
    #print (temp2)
    domains.append(temp2)
#print (domains)
dic = dict()
for domain in domains:
    dic[domain] = dic.get(domain,0)+1
for key in sorted(dic):
    print (key,':',dic[key])