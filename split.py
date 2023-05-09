def split(string):
    
    last_space = -1
    words = []

    for i in range(len(string)):

        if string[i] == ' ':
            if i == last_space + 1:
                last_space = i
                continue

            words.append(string[last_space + 1: i])
            last_space = i

        if i == len(string) - 1 and string[i] != ' ':
            words.append(string[last_space + 1: i + 1])

    
    return words

print(split("   To       be          or           not    to be,     that is    the      question     "))
print(split("To be or not to be,that is the question"))
print(split("   "))
print(split(" abc "))
print(split(""))




