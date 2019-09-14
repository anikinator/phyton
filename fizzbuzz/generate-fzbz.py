# Generate file for FizzBazz App
import random

rawdata = open('rawdata.txt','w+')

for i in range (20):
    fizz = str(random.randint(2,10))
    bazz = str(random.randint(10,30))
    number = str(random.randint(18,40))
    rawdata.write(fizz + " " + bazz + " " + number + "\n")