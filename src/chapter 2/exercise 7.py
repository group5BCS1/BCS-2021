dollars = float(input("Enter amount to change in dollars :"))
# 20 dollar notes
num1 = dollars//20
# remainder after 20
num2 = dollars%20
# notes by 10
num3 = num2//10
# remainder after 10
num4 = num2%10
# notes by 5 dollar
num5 = num4//5
# remainder after 5 dollars
num6 = num4%5
# notes by 1 dollar
num7 = num6//1
#remiander after 1 dollar
num8 = num6%1
# cents
#cents by 0.25 dollars
num9 =num8//0.25
# remainder after quarter
num10 = num8%0.25
# the dimes
num11 = num10//0.1
# remainder after the dimes
num12 = num10%0.1
# the nickles
num13 = num12//0.05
# the remainder after the nickles
num14 = num12%0.05
# the pennies
num15 = num14//0.01
print(int(num1),"twenties")
print(int(num3),"tens")
print(int(num5),"fives")
print(int(num7),"ones")
print(int(num9),"quarters")
print(int(num11),"dimes")
print(int(num13),"nickles")
print(int(num15),"pennies")
