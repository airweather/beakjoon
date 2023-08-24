alphabet = [-1] * 26
text = input()

for idx, char in enumerate(text):
    if alphabet[(ord(char)-97)] == -1:
        alphabet[(ord(char)-97)] = idx

print(" ".join(map(str, alphabet)))