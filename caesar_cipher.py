
def encrypt(string):
    encrypted = ''
    for char in string:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        encrypted += chr(code)
    
    return encrypted

def decrypt(encrypted):
    decrypted = ''
    for char in encrypted:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        decrypted += chr(code)
        
    return decrypted

cipher = input("Enter your message: ")

print(encrypt(cipher))

print(decrypt(encrypt(cipher)))
