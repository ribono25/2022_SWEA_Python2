# 4-02.py

data = input()
data_list = data.split(' ')

for i in range(0, len(data_list)):
    answer_word = data_list[-(i+1)]
    print(answer_word, end = " ")