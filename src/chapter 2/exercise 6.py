# This program calculates the distance between two points
# for first point(x1,y1):
x1 = int(input('Enter value for x1 :'))
y1 = int(input('enter value for y1 :'))
# for second point(x2,y2) :
x2=int(input('enter value for x2 :'))
y2=int(input('Enter value for y2 :'))
# for d,the distance between the two points:
d=((((x2-x1)**2)+((y2-y1)**2))**0.5)
print("distance between the two points",(x1,x2) ,'and', (y1,y2),'is',d)