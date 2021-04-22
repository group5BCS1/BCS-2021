#this program reads various  numbers from the user and prints out their total , count and average.
count = 0
total = 0
average = 0
while True :
    x = input("Enter a number:")
    if x == "done":
        break
    else:
        try:
            x = float(x)
            count = count +1
            print("Enter a number or 'done' if you are done")
            total = total +x
            average = (total/count)
            continue
        except:
                print("Invalid input , this is not a number !!!!")
                continue

print( "Your total =", total , "count=", count , "Average=", average)
