#from collections import Counter
#
#text = Counter(input().upper()).most_common()
#
#if(len(text) == 1):
#    print(text[0][0])
#elif(text[0][1] == text[1][1]):
#    print('?')
#else:
#    print(text[0][0])

from collections import Counter

def find_most_common_character(text):
    text = Counter(text.upper())
    most_common = text.most_common()
    
    if len(most_common) == 1:
        return most_common[0][0]
    elif most_common[0][1] == most_common[1][1]:
        return '?'
    else:
        return most_common[0][0]

user_input = input("Enter text: ")
result = find_most_common_character(user_input)
print(result)
