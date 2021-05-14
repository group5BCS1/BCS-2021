name = input("Enter a file name :")
name = name.lower()
handle = open(name)
for line in handle:
    line = line.upper()
    print(line)

