# 튜플과 for 문

# 2-14.py

data_tuple = tuple(range(0, 11, 2))

for item in data_tuple:
    print(format(item), end=" ")

print()

for idx, item in enumerate(data_tuple):
    print("data_tuple[%d] => %d" % (idx, item))