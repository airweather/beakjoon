# decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# number, base = input().split()
# base = int(base)

# convertedNumber = 0

# for idx, num in enumerate(reversed(number)):
    
    
#     if(num in decimal):
#         # num = int(num) * (base**idx)
#         # if(num > base):
#         #     break
#         # else: convertedNumber += num
#         convertedNumber += int(num) * (base**idx)
#     else:
#         # num = (ord(num) - 55) * (base**idx)
#         # if(num > base):
#         #     break
#         # else: convertedNumber += num
#         convertedNumber += (ord(num) - 55) * (base**idx)

# print(convertedNumber)

number, base = input().split()
print(int(number, int(base)))