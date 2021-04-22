largest = None
smallest = None
while True:
    num = input("Enter your number :")
    try:
        if num == "done":
            break
        float(num)
    except:
        print("invalid input , this is not a number !!!!")
        continue
    if smallest is None or largest is None:
        smallest = num
        largest = num
    elif num < smallest :
        smallest = num
    elif num > largest :
        largest = num
print("Maximum is " , largest)
print("Minimum is " , smallest)




