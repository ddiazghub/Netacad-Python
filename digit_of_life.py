def digitOfLife(birthday):

    if len(birthday) != 8:
        print("Invalid birthday format")
        return
    digits = [char for char in birthday]
    total_sum = 0
    for digit in digits:
        total_sum += int(digit)

    result = str(total_sum)
    while len(result) > 1:
        total_sum = 0
        for digit in result:
            total_sum += int(digit)
        
        result = str(total_sum)

    print(result)

digitOfLife(input("Enter your birthday: "))



