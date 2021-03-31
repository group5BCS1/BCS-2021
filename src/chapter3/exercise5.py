# the algorithm prompts the user for the people attending a wedding and prints the corresponding price
people = int(input("Please enter the number of people attending the wedding : "))
if 1<=people<=50:
    print("The cost of the wedding is : $4,000")
elif 0==people:
    print("The cost of the wedding is : $0")
elif 50<people<=100:
    print("The cost of the wedding is : $10,000")
elif 100<people<=200:
    print("The cost of the wedding is : $15,000")
elif people>200:
    print("The cost of the wedding is : $20,000")
else:
    print("there are no negative people")