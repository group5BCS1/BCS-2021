def computepay(hours,rate):
    hours = int(input("Enter hours :"))
    rate = float(input("Enter rate :"))
    if hours<=40:
       pay=rate*hours
    else:
       pay=(rate*40)+(1.5*(hours-40)*rate)
    return pay
payment=computepay("hours","rate")
print(payment)

