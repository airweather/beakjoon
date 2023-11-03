text_list = []

for i in range(5):
    text_list.append(list(input()))
    
max_length = max(len(sublist) for sublist in text_list)

for i in range(max_length):
    for j in range(5):
        if len(text_list[j]) > i:
            print(text_list[j][i] ,end="")