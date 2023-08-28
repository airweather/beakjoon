text = input()
dial = 0

for char in text:
    if 'P' <= char <= "S":
        dial += 8
    elif 'T' <= char <= "V":
        dial += 9
    elif 'W' <= char <= "Z":
        dial += 10
    else:
        dial += (ord(char)-65)//3+3

print(dial)