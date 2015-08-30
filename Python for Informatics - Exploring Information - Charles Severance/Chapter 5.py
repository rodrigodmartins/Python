__author__ = 'Rodrigo'

## Exercise 5.1

#list = []
#while True:
#    value = input('Enter a number: ')
#    if value == 'done':
#       break
#    try:
#        value = int(value)
#        list.append(value)
#    except:
#        print('Please enter a number')
#if len(list) != 0 :
#    print('Sum :',sum(list),'| Count :',len(list),'| Mean value :',round(((sum(list))/len(list)),2))
#else: print('No values to calculate')

## Exercise 5.2

list = []
while True:
    value = input('Enter a number: ')
    if value == 'done':
       break
    try:
        value = int(value)
        list.append(value)
    except:
        print('Please enter a number')
if len(list) != 0 :
    print('Minimum value :',min(list))
    print('Maximum value :',max(list))
else: print('No values to calculate')