# 연습문제 2

# 2-02.py

data_str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
data_list = list(data_str)

count = [data_list.count('a'), data_list.count('e'), data_list.count('i'), data_list.count('o'), data_list.count('u')]

info = ['a', 'e', 'i', 'o', 'u']
for idx, item in enumerate(count):
    for j in range(item):
        data_list.remove(info[idx])

print(''.join(map(str, data_list)))
