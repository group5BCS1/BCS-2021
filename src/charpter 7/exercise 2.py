name = input("Enter a file name :")
name = name.lower()
handle = open(name)
count = 0
total = 0
for line in handle:
    line = line.upper()
    if line.startswith('X-DSPAM-CONFIDENCE:'):
        count = count + 1
        flt = line[19:]
        flot = float(flt)
        total = (total + flot)
Spam_Confidence = total / count
print("File name :", name)
print("Average_Spam_Confidence=", Spam_Confidence)
