c = int(input("Enter intial amount of investment :"))
r = float(input("Enter the rate :"))
n = float(input("enter the number of times :"))
t = float(input("Enter the number of time for maturation :"))
def investment(c,r,t,n):
    return c*((1+(r/n))**(t*n))
print(round(investment(c,r,t,n),2))
