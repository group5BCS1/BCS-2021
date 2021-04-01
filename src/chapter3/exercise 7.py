location = input("Enter the location :")
pay = float(input("Enter the pay :"))
if pay>4000000 and location=='mbarara':
    print("Without a doubt, i'll take it")
elif pay>=10000000 and location=='kampala':
    print("sure i can work with that")
elif pay<10000000 and location=='kampala':
    print("No way")
elif pay>=0 and location=='space':
    print("Without a doubt, I'll take it")
elif pay==6000000 and location!="mbarara" "kampala" "space":
    print("sure, i can work with this")
else:
    print("No thanks, I can find something better")