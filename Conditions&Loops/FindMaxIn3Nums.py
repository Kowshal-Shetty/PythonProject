num1 = float(input("Enter the num1"))
num2 = float(input("Enter the num2"))
num3 = float(input("Enter the num3"))

if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greater")
elif num1==num2 and num1==num3:
    print("all are equal")
else:
    print("num3 is greater")