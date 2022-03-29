# 3-05.py

fruit = ['   apple    ','banana','  melon']

for i in range(len(fruit)):
    fruit[i] = fruit[i].strip()

ansdict = { key: len(key) for key in fruit }
print(ansdict) 