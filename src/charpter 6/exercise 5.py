str = 'X-DSPAM-Confidence: 0.8475 '
num = str.find(':')
print("The string after the colon is after index :", num)
flt = str[19:]
flt = float(flt)
print("The floating number is :", flt)
