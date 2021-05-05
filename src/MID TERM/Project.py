# This program is for calculating the amount of money to be paid by a customer basing on his/her meter readings and
# his code.
print("======================RESTART==============================")
print("...........You are most welcome our dear customer.......... ")
while True:
    # Customer's details
        a = str(input("Please, Enter your code :"))
        a = a.upper()
        b = int(input("Enter initial meter reading :"))
        b_str = str(b)
        z = b_str.zfill(9)
        x = int(input("Enter your final meter reading:"))
        x_str = str(x)
        y = x_str.zfill(9)
    # In case the final is less than initial
        if x < b:
                  d = ((1000000000 - b) + x) / 10
        else:
               d = (x - b) / 10
        try:
            # For residential customers
              if a == 'R':
                       e = (5.00 + (0.0005 * d))
                       print("Customer's code:", a)
                       print("Customer's initial meter reading:", z)
                       print("Customer's final meter reading:", y)
                       print("Gallons of water used :", d,"gallons")
                       print("Amount of money billed = $", (round(e, 2)))
              elif a == 'C':
                    # For commercial customers
                       if d <= 4000000:
                             e = 1000.00
                       else:
                            e = 1000 + ((d - 4000000) * 0.00025)
                       print("Customer's code:", a)
                       print("Customer's initial meter reading:", z)
                       print("Customer's final meter reading:", y)
                       print("Gallons of water used :", d,"gallons")
                       print("Amount of money billed = $", (round(e, 2)))
              elif a == 'I':
                    # For industrial customers
                       if d <= 4000000:
                                   e = 1000
                       elif 4000000 < d <= 10000000:
                                                  e = 2000
                       else :
                             e = ((d - 10000000) * 0.00025) + 2000
                       print("Customer's code:", a)
                       print("Customer's initial meter reading:", z)
                       print("Customer's final meter reading:", y)
                       print("Gallons of water used :", d,"gallons")
                       print("Amount of money billed = $", (round(e, 2)))
              else:
                  # For invalid customer codes
                   if a != 'r' or 'c' or 'i':
                                           e = (0)
                                           print("Invalid Customer Code , Please try again. Thank you.")
                                           break
        except:
             print()
# THE END