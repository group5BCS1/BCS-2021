# the program tells if one is eligible to vote or not depending on one's age
age=int(input("Enter your age please :"))
if age>=18:
    print("you can vote :")
elif 0<=age<=17:
    print("Too young to vote")
else:
    print("you are a time traveller")

