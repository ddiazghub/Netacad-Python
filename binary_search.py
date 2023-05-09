import random

list = []

for i in range(random.randrange(100)):
    list.append(random.randrange(1000))

start = 0
end = len(list) - 1
index = -1

to_find = list[random.randrange(len(list) - 1)]

# List needs to be sorted to implement binary search.
swaps = True
while swaps:
    swaps = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            swaps = True


print("List: ", list)
print("To find: ", to_find, "\n")

while end >= start:
    middle = (end - start) // 2
    if list[middle] == to_find:
        index = middle
        break
    if to_find > middle:
        start = middle + 1
    if to_find < middle:
        end = middle - 1

if index != -1:
    print("Element found at index", index)
else:
    print("absent")