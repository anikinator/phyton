def yell(any_text):
    return any_text.upper() + "!"

bark = yell

bark("hello")

del yell

bark("hey there?")

print(bark.__name__)
print(bark.__qualname__)

list_of_func = [bark, str.upper, str.lower]

for func in list_of_func:
    print(f"{func}: ",func('some text'))

list_of_func[0]("this is a man's world")

def func_with_func(func,some_text):
    return func(some_text)

print(func_with_func(bark, "hello and hello and 1000 times"))

list_and_map = list(map(bark, ["hello","world","the text of the book"]))
print(list_and_map)