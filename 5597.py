students = list(range(1,31))

for i in range(28):
    students.remove(int(input()))

for student in students:
    print(student)