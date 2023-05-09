def isPalindrome(string):

    words = string.lower().split()
    words = ''.join(words)

    for i in range(len(words)):
        if words[i] != words[-1 - i]:
            return False

    return True

string = input("Enter a string: ")

if isPalindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome")