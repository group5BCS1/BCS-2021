def chop(lst):
    del lst[0]
    del lst[-1]


def middle(lst):
    new = lst[1:]
    del new[-1]
    return new
n = int(input("Enter the number of elements :"))
list = []
for i in range(n):
    element = input("Enter the element :")
    list.append(element)
chop_list = chop(list)
print(list)
print(chop_list)

n = int(input("Enter the number of elements :"))
list2 = []
for i in range(n):
    element = input("Enter the element :")
    list2.append(element)
middle_list2 = middle(list2)
print(list2)
print(middle_list2)
