def find_word(word, string):

    current_pos = -1

    for char in word:
        if string.find(char) <= current_pos:
            return False
        
    return True

string = input("Enter a string: ")
word = input("Enter a word to find hidden on the string: ")

print(find_word(word, string))