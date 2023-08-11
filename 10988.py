text = input()
flag = 1

for i in range(len(text)//2):
    if(text[i] != text[len(text)-i-1]):
        flag = 0
        
print(flag)