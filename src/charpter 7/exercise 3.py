# Enter a file name
name = input("Enter a file name :")
# Converting to lower case in order to cater for both upper and lower cases
name = name.lower()
# For valid / defined file names
if name == 'measles.txt':
    handle = open(name)
    count = 0
    for lines in handle:
        count = count + 1    # Counting the number of lines in a file (line by line)
    print("There were ", count, " ", "Subject lines in the file :", name)
elif name == 'measles.short.txt':
    handle = open(name)
    count = 0
    for lines in handle:
        count = count + 1
    print("There were ", count, " ", "Subject lines in the file :", name)  # print count
elif name == 'mbox-short.txt':
    handle = open(name)
    count = 0
    for lines in handle:
        count = count + 1
    print("There were ", count, " ", "Subject lines in the file :", name)
elif name == 'mbox.txt':
    handle = open(name)
    count = 0
    for lines in handle:
        count = count + 1
    print("There were ", count, " ", "Subject lines in the file :", name)
# For an Easter egg
elif name == 'na na boo boo':
    print('HAHAHAHAHA   YOU ARE THE GUY BRO !!!!!!!')
# If file name is invalid
else:
    print('File can not be opened:', name)
# THE END , BY JAMESBOND BUSINESS
