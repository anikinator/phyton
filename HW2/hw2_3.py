# FizzBazz App

fizz = int(input("Enter Fizz: "))
bazz = int(input("Enter Bazz: "))
fizzbazz = int(input("Enter max number: "))

# fizz = 2
# bazz = 5
# fizzbazz = 18

result = ''

for i in range(1,(fizzbazz+1)):
    if (i % fizz == 0) and (i % bazz == 0):
        result += 'FB '
    elif (i % bazz) == 0:
        result += 'B '
    elif (i % fizz) == 0:
        result += 'F '
    else:
        result += str(i) + ' '

print("Calculated result is: " + result)