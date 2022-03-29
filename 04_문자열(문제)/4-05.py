# 4-05.py

data = '산 하늘 강 바다 하늘 강 들'
data_list = list(set(data.split()))

data_list = sorted(data_list)

print(','.join(data_list))