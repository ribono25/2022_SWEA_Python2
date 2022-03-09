# 리스트 항목 변경

# 2-05.py

data_list = [10,20,30,40]

data_list[2] = 29
print("data_list: {0}".format(data_list))

data_list[1:3] = [12, 15] # index 1, 2
print("data_list: {0}".format(data_list))

data_list[1:3] = [12, 15, 20] # 바로 뒤에 추가로 삽입됨
print("data_list: {0}".format(data_list)) # 리스트 크기 변경됨

data_list[2:3] = [31, 25] # data_list[2] = [31, 25] 와는 다른 결과를 초래함
print("data_list: {0}".format(data_list))