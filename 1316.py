count = 0

for _ in range(int(input())):
    alphabet = set()

    lastWord = ""
    
    for word in input():
        if(lastWord == word):
            lastWord = word
            continue
        else:
            if word in alphabet:
                break
            else:
                alphabet.add(word)
                lastWord = word
    else:
        count += 1
        
print(count)