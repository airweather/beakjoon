# alphabet = [-1] * 26
# text = input()

# for idx, char in enumerate(text):
#     if alphabet[(ord(char)-97)] == -1:
#         alphabet[(ord(char)-97)] = idx

# print(" ".join(map(str, alphabet)))

alphabet = {}
text = input()

for idx, char in enumerate(text):
    if char not in alphabet:
        alphabet[char] = idx
    print(alphabet)

result = [alphabet.get(chr(97 + i), -1) for i in range(26)]
print(" ".join(map(str, result)))