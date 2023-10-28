# count = 0

# for _ in range(int(input())):
#     alphabet = set()

#     lastWord = ""
    
#     for word in input():
#         if(lastWord == word):
#             lastWord = word
#             continue
#         else:
#             if word in alphabet:
#                 break
#             else:
#                 alphabet.add(word)
#                 lastWord = word
#     else:
#         count += 1
        
# print(count)

count = 0

for _ in range(int(input())):
    unique_chars = set()
    word = input()
    
    for i, char in enumerate(word):
        if i > 0 and char != word[i - 1] and char in unique_chars:
            break
        unique_chars.add(char)
    else:
        count += 1

print(count)