text = input()
count = 0
size = len(text)

i = 0
while i < size:
    if(i == size-1):
        count += 1
        break
    if(text[i] =='c'):
        if(text[i+1] == '=' or text[i+1] == '-'):
            count += 1
            i += 2
            continue
    if(text[i] =='d'):
        if(text[i+1] == 'z' and i < size-2):
            if(text[i+2] =='='):
                count += 1
                i += 3
                continue
        if(text[i+1] == '-'):
            count += 1
            i += 2
            continue
    if(text[i] =='l'):
        if(text[i+1] == 'j'):
            count += 1
            i += 2
            continue
    if(text[i] =='n'):
        if(text[i+1] == 'j'):
            count += 1
            i += 2
            continue
    if(text[i] =='s'):
        if(text[i+1] == '='):
            count += 1
            i += 2
            continue
    if(text[i] =='z'):
        if(text[i+1] == '='):
            count += 1
            i += 2
            continue
    count += 1
    i += 1

print(count)