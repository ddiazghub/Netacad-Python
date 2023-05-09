def read_int(prompt, min, max):
    try:
        number = int(input(prompt))
        assert number >= min and number <= max
        return number
    except ValueError:
        print("Error: wrong input")
        return read_int(prompt, min, max)
    except AssertionError:
        print("Error: the value is not within permitted range (min..max)")
        return read_int(prompt, min, max)



v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
