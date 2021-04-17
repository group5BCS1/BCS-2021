def investment(c,r,n,t):
    p=c*1+(c*r/n)**(t*n)
    return p
result=investment (10000,0.01,1,1)
print("The pay =",round(result,2))