number, base = map(int, input().split())

convertedNumber = ""

def convert(num):
    if(num < 10):
        return str(num)
    else:
        return chr(num + 55)

while number > 0:
    convertedNumber = convert(number%base) + convertedNumber
    number = number // base

print(convertedNumber)