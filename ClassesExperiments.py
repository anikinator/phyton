class MyFor:
    a = 5

    def __init__(self, *args):
        print("="*25,self,"="*25)

    def MyCustomPrint(self, a="default"):
        print(a)

    b = 20

instance1 = MyFor()
instance1.MyCustomPrint("My sustom string")

instance2 = MyFor()
instance2.MyCustomPrint()

# print(dir(MyFor))
print(instance1.b)

print(instance2.b)