score = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

credit = 0
totalScore = 0

for i in range(20):
    data = input().split()
    if(data[2] == "P"):
        continue
    credit = credit + float(data[1])
    totalScore = totalScore + (float(data[1]) * (score[data[2]]))

print(totalScore/credit)