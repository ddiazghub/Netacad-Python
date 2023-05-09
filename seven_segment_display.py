


def seven_segment(number):

    numbers = {
        '0': ['###', '# #', '# #', '# #', '###'],
        '1': ['  #', '  #', '  #', '  #', '  #'],
        '2': ['###', '  #', '###', '#  ', '###'],
        '3': ['###', '  #', '###', '  #', '###'],
        '4': ['# #', '# #', '###', '  #', '  #'],
        '5': ['###', '#  ', '###', '  #', '###'],
        '6': ['###', '#  ', '###', '# #', '###'],
        '7': ['###', '  #', '  #', '  #', '  #'],
        '8': ['###', '# #', '###', '# #', '###'],
        '9': ['###', '# #', '###', '  #', '###'],
    }

    digits = list(str(number))
    led_matrixes = []
    
    for i in range(5):
        row = [numbers[digit][i] for digit in digits]
        led_matrixes.append(' '.join(row))

    print('\n'.join(led_matrixes))

number = input("Input a number: ")
seven_segment(number)

