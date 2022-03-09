# 리스트 항목 접근

# 2-02.py

data_list = [10, 20, 30, 40, 50]

print("data_list: {0}".format(data_list))

print("data_list[%d] => %d" % (0, data_list[0])) # 인덱스 0 : 첫 번째 항목
print("data_list[%d] => %d" % (1, data_list[1]))
print("data_list[%d] => %d" % (2, data_list[2]))
print("data_list[%d] => %d" % (3, data_list[3]))
print("data_list[%d] => %d" % (4, data_list[4])) # 인덱스 4 : 마지막 항목

# 원소의 개수 - 1 = 마지막 인덱스 번호

print("data_list[%d] => %d" % (-5, data_list[-5]))
print("data_list[%d] => %d" % (-4, data_list[-4]))
print("data_list[%d] => %d" % (-3, data_list[-3]))
print("data_list[%d] => %d" % (-2, data_list[-2]))
print("data_list[%d] => %d" % (-1, data_list[-1]))

# 마지막 인덱스 번호 : -1
# 왼쪽으로 갈 때마다 1씩 감소

try:
    print("data_list[5] => %d" % data_list[5])
except IndexError as I:
    print(I)

print("data_list[0:3] => {0}".format(data_list[0:3])) # 인덱스 범위 지정 = 콜론(:)
print("data_list[-5:-2] => {0}".format(data_list[-5:-2])) # 시작 인덱스 값 ~ 종료 인덱스 값 + 1

print("data_list.index(20) => %d" % data_list.index(20)) # 해당 값이 들어 있는 인덱스 값 반환 (중복 시 첫 번째 인덱스 값)