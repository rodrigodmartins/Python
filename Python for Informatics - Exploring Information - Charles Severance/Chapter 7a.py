__author__ = 'Rodrigo'

#file = open('output.txt','w')
#file.write('Rodrigo\n')
#file.write('Dias\n')
#file.write('Martins\n')
#file.close()

##Exercise 7.1
# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
# Executing the program will look as follows:

#file = input('Please inform the name of the txt file (without extension): ')
#file2 = file.lower()
#file3 = file2+'.txt'
#file4 = open(file3)
#file5 = file4.read()
#print(file5.upper())

##Exercise 7.2
# Write a program to prompt for a file name, and then read through the file and look for lines of the form:

#file = input('Please inform the name of the txt file (without extension): ')
#file2 = file.lower()
#file3 = file2+'.txt'
#file4 = open(file3)
#
#count = 0
#total = float(0)
#for lines in file4:
#    if lines.startswith('X-DSPAM-Confidence:'):
#        count += 1
#        temp = lines
#        p1 = temp.find(' ')
#        number = temp[p1+1:]
#        total += float(number)
#
#print ('Number of lines with "X-DSPAM-Confidence:"',count)
#print ('Sum of all DSPAM confidence intervals:',total)
#print ('Average value of DSPAM confidence intervals:',(total/count))

##Exercise 7.3
# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program
# (en.wikipedia.org/wiki/Easter_egg_(media)).


name = input('Please inform the name of the txt file (without extension): ')
name2 = name.lower()
name3 = name2+'.txt'
if name2 == 'na na boo boo':
    name4 = name2.upper()
    print ("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
else:
    print('Looking for',name3,'file ...')
try:
    lines = open(name3)
    print ('File',name3,'found !')
    count = 0
    for line in lines:
        count += 1
    print('The file',name3,'has',count,'lines.')
except:
    print('File cannot be opened:',name3)