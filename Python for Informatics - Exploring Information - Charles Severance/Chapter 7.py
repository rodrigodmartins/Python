__author__ = 'Rodrigo'

fhand = open('mbox.txt')
#print(fhand)

count = 0
for lines in fhand:
    count+=1
print('The file has',count,'lines')

fhand = open('mbox-short.txt')
fhand2 = fhand.read()
print(fhand2[:20])
print('The file has',len(fhand2),'characters')

#fhand = open('mbox.txt')
#for line in fhand:
#    if line.startswith('From:'):
#        line2=line.rstrip()
#        print(line2)

#fhand = open('mbox.txt')
#for line in fhand:
#    if line.find('@uct.ac.za') != -1:
#        line2=line.rstrip()
#        print(line2)



def count():
    name = input('Please inform the name of the txt file (without extension): ')
    name2 = name.lower()
    name3 = name2+'.txt'
    print('Looking for',name3,'file ...')
    try:
        lines = open(name3)
        print ('File',name3,'found !')
        count = 0
        for line in lines:
            count += 1
        print('The file',name3,'has',count,'lines.')
    except:
        print('File not found !!!')

count()
while True:
    answer = input('Do you want to look for another file? [y/n]: ')
    answer2 = answer.lower()[0]

    if answer2 == 'y':
        count()
    else:
        exit()