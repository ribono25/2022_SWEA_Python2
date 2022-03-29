# 4-04.py

datalist = []
while True:
    data = input()

    if not data:
        break

    datalist.append(data)

for val in datalist:
    print(f'>> {val.upper()}')