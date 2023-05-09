# Punto 1:

# Función
def sum(lst, i):
    if i < len(lst):
        return lst[i] + sum(lst, i+1)
    else:
        return 0


# Subrutina
def divisors(number, divisor, i):
    if i > 1:
        if number % i == 0:
            divisor.append(number)
        divisors(number, divisor, i - 1)


# Subrutina
def prime_nums(matrix, primes, i, j):
    if i < len(matrix):
        if j < len(matrix[i]):
            divisor = []
            divisors(matrix[i][j], divisor, matrix[i][j] // 2)
            if len(divisor) == 0:
                primes.append(matrix[i][j])
            prime_nums(matrix, primes, i, j + 1)
        else:
            prime_nums(matrix, primes, i + 1, 0)


# Punto 2:

# Función
def hex_digit(digit):
    digits = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    try:
        return digits[digit]
    except KeyError:
        return str(digit)


# Función
def to_hex(number):
    if number > 0:
        digit = number % 16
        return to_hex(number // 16) + hex_digit(digit)
    else:
        return ''


# Punto 3:

# Subrutina
def to_hex_vector(matrix, hex_vector, i, j):
    if i < len(matrix):
        if j < len(matrix[i]):
            if matrix[i][j] == 0:
                hex_vector.append('0')
            else:
                hex_vector.append(to_hex(matrix[i][j]))
            to_hex_vector(matrix, hex_vector, i, j + 1)
        else:
            to_hex_vector(matrix, hex_vector, i + 1, 0)


# Función
def deficient_nums(matrix, i, j):
    if i < len(matrix):
        if j < len(matrix[i]):
            divisor = []
            divisors(matrix[i][j], divisor, matrix[i][j] // 2)
            sumD = sum(divisor, 1)
            if sumD < matrix[i][j]:
                return deficient_nums(matrix, i, j + 1) + 1
            else:
                return deficient_nums(matrix, i, j + 1)
        else:
            return deficient_nums(matrix, i + 1, 0)
    else:
        return 0


matrix = [[i * 5 + j for j in range(5)] for i in range(5)]
print("Matriz: ", matrix)
primes = []
hex_vector = []
prime_nums(matrix, primes, 0, 0)
to_hex_vector(matrix, hex_vector, 0, 0)
print("Punto 1: ", primes)
print("Punto 2: ", hex_vector)
print("Punto 3: ", deficient_nums(matrix, 0, 0))