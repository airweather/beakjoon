from collections import Counter

text = Counter(input().upper()).most_common()

if(len(text) == 1):
    print(text[0][0])
elif(text[0][1] == text[1][1]):
    print('?')
else:
    print(text[0][0])