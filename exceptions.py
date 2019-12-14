class MyCustomBaseException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return f"{self.args}, {self.kwargs}"


class OtherCustomException(MyCustomBaseException):
    pass


class AlwaysRaiseExceptionClass:
    def __new__(cls, *args, **kwargs):
        # raise BaseException
        # raise Exception("My custom message", "Another arg")
        # raise MyCustomBaseException(3, 2, 1, my_data="TEST")
        raise OtherCustomException(1, 2, 3, my_data="TEST")


try:
    AlwaysRaiseExceptionClass()
except MyCustomBaseException as e:
    print(e)
except Exception as e:
    print(e)
except:
    print("LAST CHANCE TO HANDLE ALL")


class Test:
    def __bool__(self):
        return False


# assert Test()