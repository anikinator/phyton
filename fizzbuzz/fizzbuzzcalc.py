# Calc fizzbazz and write to file result.txt
import sys

rawdata = open('rawdata.txt','r')
resultdata = open('fizzbazz.txt','w+')

for rawstring in rawdata:
    rawstring = rawstring.split()
    print(rawstring)

    result = ''

    fizz = int(rawstring[0])
    bazz = int(rawstring[1])
    number = int(rawstring[2])

    for i in range(1,number+1):

        if (i % fizz == 0) and (i % bazz == 0):
            result += 'FB '
        elif (i % bazz) == 0:
            result += 'B '
        elif (i % fizz) == 0:
            result += 'F '
        else:
            result += str(i) + ' '
    resultdata.write(result + '\n')

    rawdata.close()
    resultdata.close()

print("Please, check fizzbazz.txt")