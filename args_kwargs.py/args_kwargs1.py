def foo(*args,**kwargs):
    print(args)
    #b = (*args)
    print(type(args))
    print(f"Prosto {args}")
    print(*args)
    print(kwargs)


foo(1,2,3,"str1",key1=[1,3,4,8],key2="some value",mytuple=("peta","vasa","maxim"))
tuple1 = (1,2,3,"str1",4,2,1,6,3,4,1,10)
print(tuple1)

def print_vector(x,y,z):
    print(f"<{x} {y} {z}>")

genexpr = (x * x for x in range(3))
print_vector(*genexpr)


# class Customer():
#     def __init__(self, budget):
#         # self.budget = budget
#         self.budget = self.validate_budget(budget)

#     def validate_budget(self, budget):
#         if budget > 0:
#             return budget
#         else:
#             return 1

#     def discount(self, bbb):
#         return bbb.price * 1

#     def pur_pow(self, aaa):
#         return self.budget // self.discount(aaa)

# mycustomer = Customer(35)
# print(mycustomer.budget)