int_age = int(input("Enter the age"))

if int_age>=18 :
    print("You are allowed to vote")
else:
    print("You are not allowed to vote")



print("Allowed to vote" if int_age>=20 else "Not allowed to vote")