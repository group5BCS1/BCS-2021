def open_file():
    while True:
        try:
            user_file = input("Enter file name: ")
            file_ = open(user_file, "r")
            break
        except:
            print("Invalid file name:")
    return file_


def process_file(file_object):
    try:
        income_level_display = """
        1 = low_income
        2 = lower middle income
        3 = upper middle income
        4 = high income"""
        low_income = "WB_LI "
        lower_middle_income = 'WB_LMI '
        upper_middle_income = "WB_UML "
        high_income = "WB_HL "
        year = input("Enter a year; ")
        income_level = input(f"{income_level_display}\n Enter the income lever")
        count = 0
        total = 0
        max_percent = None
        min_percent = None
        country_max = []
        country_min = []
        for line in file_object:
            if year == line[88:92]:
                if income_level == "1":
                    if line[51:57] == low_income:
                        percentage = float(line[58:61])
                        count += 1
                        total += percentage
                        if max_percent is None or max_percent < percentage:
                            max_percent = percentage
                            if float(line[58:61]) == max_percent:
                                country_max.append(line[0:49])
                        if min_percent is None or min_percent > percentage:
                            min_percent = percentage
                            if float(line[58:61]) == min_percent:
                                country_min.append(line[0:49])
                        continue
                if income_level == "2":
                    if line[51:57] == lower_middle_income:
                        percentage = float(line[58:61])
                        count += 1
                        total += percentage
                        if max_percent is None or max_percent < percentage:
                            max_percent = percentage
                            if float(line[58:61]) == max_percent:
                                country_max.append(line[0:49])
                        if min_percent is None or min_percent > percentage:
                            min_percent = percentage
                            if float(line[58:61]) == min_percent:
                                country_min.append(line[0:49])
                        continue
                elif income_level == "3":
                    if line[51:57] == upper_middle_income:
                        percentage = float(line[58:61])
                        count += 1
                        total += percentage
                        if max_percent is None or max_percent < percentage:
                            max_percent = percentage
                            if float(line[58:61]) == max_percent:
                                country_max.append(line[0:49])
                        if min_percent is None or min_percent > percentage:
                            min_percent = percentage
                            if float(line[58:61]) == min_percent:
                                country_min.append(line[0:49])
                        continue
                elif income_level == "4":
                    if line[51:57] == high_income:
                        percentage = float(line[58:61])
                        count += 1
                        total += percentage
                        if max_percent is None or max_percent < percentage:
                            max_percent = percentage
                            if float(line[58:61]) == max_percent:
                                country_max.append(line[0:49])
                        if min_percent is None or min_percent > percentage:
                            min_percent = percentage
                            if float(line[58:61]) == min_percent:
                                country_min.append(line[0:49])
                        continue
        print(f"There are {count} countries found in the user's criteria" )
        print(f"The average percentage for records == {round(total/count,1)}")
        print(f" The  the lowest percentage is == {country_min}")
        print(f"The the highest percentage is  =={country_max} ")
        print("")
        print('These are countries with the highest percentage')
        for item in country_max:
            print(item.strip())

        print('')
        print('These are countries with the Lowest percentage')
        for item in country_min:
            print(item.strip())

    except:
        print("Invalid Inputs")


def main():
    file_ = open_file()
    process_file(file_)


main()