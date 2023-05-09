def encrypt(string, shift = 1):
    encrypted = ''
    for char in string:
        if char.isalpha():
            code = ord(char) + shift

            if char.islower():
                if code > ord('z'):
                    code = ord('a') + (code - ord('z') - 1)

            if char.isupper():
                if code > ord('Z'):
                    code = ord('A') + (code - ord('Z') - 1)
        else:
            code = ord(char)

        encrypted += chr(code)
    
    return encrypted


def decrypt(encrypted, shift = 1):
    decrypted = ''
    for char in encrypted:
        if char.isalpha():
            code = ord(char) - shift

            if char.islower():
                if code < ord('a'):
                    code = ord('z') - (ord('a') - code - 1)

            if char.isupper():
                if code < ord('A'):
                    code = ord('Z') - (ord('A') - code - 1)
        else:
            code = ord(char)

        decrypted += chr(code)
        
    return decrypted

cipher = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))

print(encrypt(cipher, shift))

print(decrypt(encrypt(cipher, shift), shift))
