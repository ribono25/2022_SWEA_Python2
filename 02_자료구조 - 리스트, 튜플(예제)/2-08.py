# 리스트와 for 문

# 2-08.py

data_list = list(range(0, 11, 2))

for item in data_list:
    print(item, end=" ")

print()

for idx, item in enumerate(data_list):
    print("data_list[{0}] => {1}".format(idx, item))