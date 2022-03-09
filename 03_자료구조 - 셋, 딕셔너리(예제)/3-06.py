# 셋과 for 문

# 3-06.py

data_set = set(range(0, 11, 2))

for item in data_set:
    print("{0}".format(item), end=" ")

print()

for idx, item in enumerate(data_set):
    print("[{0}] => {1}".format(idx, item))