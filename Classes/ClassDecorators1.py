from datetime import datetime, timedelta

class BurthDate:
    def __init__(self, custom_date):
       self.custom_date = self.convert_date(custom_date)
       #print(self.custom_date)

    def convert_date(self, date_string):
        try:
            return datetime.strptime(date_string,"%Y-%m-%d")

        except ValueError as e:
            print(f"Your date format is incorrect, error is: {e}")

    @property
    def age(self):
        today = datetime.today()
        return  today.year - self.custom_date.year - ((today.month, today.day) < (self.custom_date.month, self.custom_date.day))

test_obj = BurthDate("1999-12-04")
test_obj1 = BurthDate("1999-12-01")

print(test_obj.age)
print(test_obj1.age)

# print("*"*80)
# custom_date1 = datetime.strptime("1999-12-02","%Y-%m-%d")
# custom_date2 = datetime.strptime("1999-12-03","%Y-%m-%d")
# today = datetime.today()
# result1 = today.year - custom_date1.year - ((today.month, today.day) < (custom_date1.month, custom_date1.day))
# result2 = today.year - custom_date2.year - ((today.month, today.day) < (custom_date2.month, custom_date2.day))
# print(result1)
# print(result2)

#print(type(today))