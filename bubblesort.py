import random

swaps = True

list = []

for i in range(random.randrange(100)):
    list.append(random.randrange(1000))

#   Lists can be sorted  with the .sort() methos
#   list.sort()

print("Original list: ", list)

while swaps:
    swaps = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            swaps = True

print("Sorted list: ", list)