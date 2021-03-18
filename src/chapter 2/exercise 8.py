c = int(input("enter initial amount:"))
r = float(input("enter yearly rate of interest:"))
t = int(input("enter number of years until maturity:"))
n = float(input("enter number of times the interest is compounded per year:"))
a = (1+(r/n))
b = (t*n)
d = a**b
p = c*d
print("The final value of investment is:""%.2f" % p)