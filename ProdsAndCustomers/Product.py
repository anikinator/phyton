class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discount(self):
        return self.price * 0.2

    @property
    def discount(self):
        return self.get_discount()

    def get_price(self):
        return self.price - self.get_discount()

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def count_products(self, prod):
        return self.budget // prod.price

class VipCustomer(Customer):
    pass

class SuperVipCustomer(Customer):
    pass

prod2 = Product(name="vine", price=42)
cust1 = Customer(name="Vasya", budget=100)

vip1 = VipCustomer(name="Petya", budget=200)

print(f"Just customer {cust1.count_products(prod2)}")
print(f"Just Vip customer {vip1.count_products(prod2)}")

# product1 = Product(name="vine", price=33)
# vip = VipCustomer(name="vasya", budget=100)
# print(vip.count_products())
