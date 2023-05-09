blocks = int(input("Enter the number of blocks: "))
height = 0

i = 1
while blocks >= 1 + i:
    blocks -= i
    height += 1
    i += 1

print("The height of the pyramid:", height)