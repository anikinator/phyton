from sys import argv

# Task 1

def makeupper(mystring):
    return mystring.upper()

def makelower(mystring):
    return mystring.lower()

mysuperstring = 'This is my Super string and it\'s cool'

print(makeupper(mysuperstring))
print(makelower(mysuperstring))

list_of_strings = ['first string', 'second string', 'third string']

print(list(map(makeupper,list_of_strings)))
print(list(map(makelower,list_of_strings)))

# Task 2

def my_personal_square(my_number):
    return my_number ** 2

print(my_personal_square(11))

list_of_simple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(my_personal_square,[i for i in range(1,101) if i % 2 !=0 ])))

print("="*50)

# Simple Numbers and Squars of it
def simple_numbers(x):

    list_of_simples = [] # list of simple

    for x in range (2,100):
        z = 0
        for y in range(2,x):
            if x % y == 0:
                z += 1
        if z == 0:
            list_of_simples.append(x)
    return list_of_simples

print(simple_numbers(100))

print(list(map(my_personal_square,simple_numbers(100))))

# Task 3
print("="*50)

def my_read_file(file_name_to_read):
    file_name_to_read = open(file_name_to_read, 'r')
    return  file_name_to_read.read().split()

global my_dict
my_dict = dict()


my_dict = dict(my_read_file("story.txt"))
print(type(my_dict))git

def test(x):
return x.upper()
    global my_dict
    if x not in my_dict:
        my_dict[x] = 1
    else:
        my_dict[x] += 1
    print(my_dict)
    return my_dict

print(list(map(word_stat, my_read_file("story.txt"))))

#print(list(map(test, my_read_file("story.txt"))))
t = list(map(test, my_read_file("story.txt")))
