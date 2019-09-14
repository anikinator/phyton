# Digits and Multipliers

x = int(input("Enter Number: "))

i = 1
counter = 0
while (x // i) != 0:
    counter += 1
    i *= 10
    y = x % i
    if y == 0:
        y = 0
    else:
        y = y // (i/10)

    print("Digit " + str(counter) + ": ", y, "| Multiplier: ",i/10)

#    unless - if not