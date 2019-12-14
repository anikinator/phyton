class User:

    def  __init__(self,*args,**kwargs):
        self.set_name(*args)

    def set_name(self,*args):
        #print(args)
        if (len(args[0]) > 0):
            self.name = args[0]

    def get_name(self):
        return self.name
#        pass

    def set_surname(self):
        pass

    def get_surname(self):
        pass

    def get_name_and_surname(self):
        pass

    def set_addresses(self):
        pass

    def set_phones(self):
        pass

    def set_password(self):
        pass

    def validate_password(self):
        pass

    def check_password(self):
        pass


user1 = User("Petya")
user2 = User("Vasya")

print(user1.name)
print(user2.name)