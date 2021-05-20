list = []                        # Initialize array
while True:
    element = 0.0
    element = input('Enter a number: ')
    if element == 'done':
        break

    try:
        element = float(element)
    except ValueError:
        print('Invalid input')
        quit()

    list.append(element)

if list:
    print('Maximum: ', max(list))
    print('Minimum: ', min(list))
