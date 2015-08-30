__author__ = 'Rodrigo'

##Exercise 6.1
#Write a while loop that starts at the last character in the string and works its way backwards to the first
#character in the string, printing each letter on a separate line, except backwards.

list =[]
word = 'Rodrigo'
index = -1
while index >= -len(word):
    print (word[index])
    list.append(word[index])
    index -= 1
print(list)



for char in word:
    print(char)

##Exercise 6.2
#Given that fruit is a string, what does fruit[:] mean?

fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[:])

##Exercise 6.3
#Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(word,letter):
    word1 = word.lower()
    letter1 = letter.lower()
    count = 0
    for i in word1:
        if i == letter1:
            count += 1
    print('The count for letter "'+letter1+'" is :',count)

# Test:
count('banana','a')
#The count for letter a is : 3
#
count('rodrigo','a')
#The count for letter  a is : 0
#
count('rodrigo','r')
#The count for letter  r is : 2


##Exercise 6.4
#There is a string method called count that is similar to the function in the previous exercise. Read the documentation
# of this method at https://docs.python.org/2/library/stdtypes.html#string-methods and write an invocation that counts
# the number of times the letter a occurs in 'banana'.

word = 'banana'
print('Count of "a" :',word.count('a'))
print('Count of "n" :',word.count('n'))


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print (atpos)

sppos = data.find(' ',atpos)
print (sppos)

host = data[atpos+1:sppos]
print (host)

##Exercise 6.5
#Take the following Python code that stores a string: str = 'X-DSPAM-Confidence: 0.8475'
#
#Use find and string slicing to extract the portion of the string after the colon character and then use the
#float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
p1 = str.find(' ')
number = str[p1+1:]
print(number)
print(type(number))
number2 = float(number)
print(number2)
print(type(number2))

##Exercise 6.6
# Read the documentation of the string methods at https://docs.python.org/2/library/stdtypes.html#string-methods.
# You might want to experiment with some of them to make sure you understand how they work. strip and replace are
# particularly useful. The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]),
# the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start,
# then end is optional.
#
#str.replace(old, new[, count])
#Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count
#is given, only the first count occurrences are replaced.
#
#str.strip([chars])
#Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying
#the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars
#argument is not a prefix or suffix; rather, all combinations of its values are stripped:

name = 'Bruce Wayne and Clark Kent'
print(name)
name2 = name.replace('Clark Kent','Peter Parker')
print(name2)

url = 'www.google.com'
print(url)
url2 = url.strip('www.')
print(url2)

