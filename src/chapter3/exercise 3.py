score = float(input('Please enter the score between 0.0 and 1.0 :'))
if score >1.0:
    print("out of range")
elif score<0.0:
    print("out of range")
elif score>=0.9:
    print("A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("C")
elif score>=0.6:
    print("D")
else:
    print("F")



