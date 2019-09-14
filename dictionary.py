import sys, collections

#s = 'my string is the best of the best'

filename = sys.argv[1]

myfile = open(filename,'r')

mydict = {}

for strings in myfile:
    s = strings

    for symbol in s:
#        print(symbol)
        if symbol in mydict:
            mydict[symbol] += 1
        else:
            mydict[symbol] = 1


sorted_dict = dict(sorted(mydict.items()))
print(sorted_dict)

for key,value in sorted_dict.items():
    print(key + ":  ", value)

myfile.close()

# s = s.split()
# for w in s:
#     print(w)