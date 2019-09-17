# List comprehension

# 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([x for x in a if x < 5])

# 2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set.intersection(set(a), set(b)))

print([elem for elem in a if elem in b])

#print([lambda elem: elem*elem for elem in a if elem in b])

x = lambda a,b,c: a+b+c
print(x(5,3,9))

result = list(filter(lambda elem: elem in b, a))
print(result)

# 3
