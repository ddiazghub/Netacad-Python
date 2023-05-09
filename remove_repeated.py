import random

list = []

for i in range(random.randrange(100)):
    list.append(random.randrange(10))

#   Lists can be sorted  with the .sort() methos
#   list.sort()

print("Original list: ", list)

new_list = []

for element in list:
    if element not in new_list:
        new_list.append(element)

del list
print("List with removed duplicates: ", new_list)