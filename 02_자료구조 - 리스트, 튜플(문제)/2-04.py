# 연습문제 4

# 2-04.py

data_list = [ int(input()) for _ in range(5)]

print("입력된 값 {0}의 평균은 {1:.1f}입니다.".format(data_list, sum(data_list)/len(data_list)))