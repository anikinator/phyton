i = res = 0
count = 0
while i < 11:
    count += 1
    res += i
    i += 1
print(res, count)

i = 10
while True:
    i -= 1
    if not i: continue
    if i%2:
        print(i)
    if i < -10: break

z = 1

while z <= 100:
    z += 1
    if z % 2 == 0:
        print(z)


#fac = int(input())
fac = 5
i = x = 1
while i <= fac:
    x = x * i
    i += 1
    print(x)

a = [10,20,30,40]
for index, item in enumerate(a):
    a[index] = item + 5
    print(index)
print(a)

s = 'my string'
for symbol in s:
    print(symbol)

print(s[0:len(s)])
