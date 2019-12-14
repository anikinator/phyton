def my_decor(func):
    print("decor logic")
    def wrapper():
        func(a,b)
        print("decor post code")
        return func
        #return func
    return wrapper

@my_decor
def test_func(*args, **kwargs):
    return print(f"Function result {args}, {kwargs}")

#result = my_decor(test_func(1,2,3,test="123"))
result = test_func(1,2)

# def benchmark(func):
#     import time

#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#     return wrapper

# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')

# fetch_webpage()