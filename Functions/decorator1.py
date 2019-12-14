def null_decor(func):
    return func

@null_decor
def greet():
    return "Hello to you"


#print(null_decor(greet))
#greet = null_decor(greet)
greet()

# decorator with wrapper
def my_uppercase(func):
    def wrapper():
        original_result = func()
        decor_result = original_result.upper()
        return decor_result
    return wrapper

@my_uppercase
def test_func():
    return "hello world?"

print(test_func())



