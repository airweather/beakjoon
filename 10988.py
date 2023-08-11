# text = input()
# flag = 1

# for i in range(len(text)//2):
#     if(text[i] != text[len(text)-i-1]):
#         flag = 0
        
# print(flag)

text = input()

if text == text[::-1]:
    print(1)
else:
    print(0)
    
# [start:end:step]
# step이 -1일 경우 역순