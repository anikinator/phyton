divider = int(input("enter number: "))

try:
    result = 100 / divider
except Exception as e:
    print(f"you can not pass {divider}, {e}")
finally:
    print("finally")