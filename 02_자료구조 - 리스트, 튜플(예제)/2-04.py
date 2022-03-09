# 리스트 항목 추가

# 2-04.py

data_list = [10,20,30,40]

print("data_list: {0}".format(data_list))

data_list.append(50) # 맨 뒤에 추가
data_list.append(60) # 반환 값 없음

print("data_list: {0}".format(data_list))

data_list.insert(2, 25) # 인덱스 번호, 값 : 인덱스 번호에 값 삽입

print("data_list: {0}".format(data_list))

data_list.extend([70, 80]) # 리스트 전달, 내부 원소 값을 맨 뒤에 추가 & 반환 값 없음 => data_list += [70, 80] 
data_list.append([90, 100]) # 리스트 [90, 100]을 원소 값으로 전달하게 됨

print("data_list: {0}".format(data_list))

