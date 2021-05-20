out_put= input('enter output file name')
year = input('enter the year')
if year.isdigit():
    with open('measles.txt', 'r') as file:
        with open(out_put, 'w') as out:
            for line in file:
                years = line[-5:]
                if years.startswith(year):
                    out.write(line)
                    print(line)
elif year == "":
    with open('measles.txt', 'r') as file:
        with open(out_put, 'w') as out:
            for line in file:
                out.write(line)
                print(line)
elif year==('all' or 'ALL'):
    with open('measles.txt', 'r') as file:
        with open(out_put, 'w') as out:
            for line in file:
                out.write(line)
                print(line)
else:
    print('error')


