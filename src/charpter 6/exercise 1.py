# Write a while loop that starts at the last character in the string and works its way backwards to the first
# character in the string, printing each letter on a separate line, except backwards.
a = input("Enter a word:")
a = a.lower()
if a == 'backwards':
    exit()
else:
    index = 0
    fruit = a
    while index < len(fruit):
        index = index - 1
        if index < -len(fruit):
            break
        letter = fruit[index]
        print(letter)
