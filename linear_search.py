import random

found = False
list = []

for i in range(random.randrange(100)):
    list.append(random.randrange(1000))

to_find = list[random.randrange(len(list) - 1)]

print("List: ", list)
print("To find: ", to_find, "\n")

for i in range(len(list)):
    found = list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")
