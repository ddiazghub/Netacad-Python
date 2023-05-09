
def areAnagrams(string1, string2):

    if string1 == string2 == '':
        return False

    string1 = ''.join(string1.lower().split())
    string2 = ''.join(string2.lower().split())

    if len(string1) != len(string2):
        return False
    
    for char in string1:
        if string1.count(char) != string2.count(char):
            return False

    return True

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if areAnagrams(string1, string2):
    print("Anagrams")
else:
    print("Not anagrams")