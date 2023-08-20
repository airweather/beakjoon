textList = list()

for i in range(int(input())):
    text = input()
    textList.append(text[0]+text[-1])

for text in textList:
    print(text)