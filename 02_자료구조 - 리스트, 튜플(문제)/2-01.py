# 연습문제 1

# 2-01.py

student_data = []

first_st = (90, 80)
second_st = (85, 75)
third_st = (90, 100)

student_data.append(first_st)
student_data.append(second_st)
student_data.append(third_st)

for idx, item in enumerate(student_data):
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:.1f}입니다.".format(idx+1, sum(item), sum(item)/2))