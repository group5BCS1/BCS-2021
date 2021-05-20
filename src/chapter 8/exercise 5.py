name = input("Enter the file name :")
file = open(name)
count = 0
for line in file:
    if line.startswith("From"):
        words = line.split()
        count = count + 1
        sender = words[1]
        print(sender)
print('There were  lines in the file with From as the first word', count)
