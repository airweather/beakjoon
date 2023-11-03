text_list = [list(input()) for _ in range(5)]
    
max_length = max(len(sublist) for sublist in text_list)

for i in range(max_length):
    for j in range(5):
        if len(text_list[j]) > i:
            print(text_list[j][i] ,end="")