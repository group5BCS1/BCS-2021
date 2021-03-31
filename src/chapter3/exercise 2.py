try:
    hours = int(input("enter hours :"))
    rate=int(input("enter rate :"))
    pay = int(hours * rate)
    print("pay")
except:
    print("Error, enter numeric input!")