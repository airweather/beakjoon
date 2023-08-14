from functools import reduce

def add(x, y):
    return x + y

numbers = list()

for i in range(5):
    numbers.append(int(input()))
    
numbers.sort()

print(int(reduce(add, numbers)/len(numbers)))

print(numbers[len(numbers)//2])