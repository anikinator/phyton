# Digits and Multipliers

x = int(input("Enter Number: "))

i = 1
counter = 0
while (x // i) != 0:
    i *= 10
    y = x % i
#    print(y)
    print("Digit: ", y, "Multiplier: ",i/10)

#    unless - if not