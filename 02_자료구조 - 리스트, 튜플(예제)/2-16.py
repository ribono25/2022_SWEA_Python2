# 리스트 객체를 활용해 총점과 평균 구하기]

# 2-16.py

account = int(input("총 학생 수를 입력하세요: "))

student_data, info = [], ['국어', '수학', '영어']
for i in range(account):
    data = [0,0,0]

    for j in range(3):
        print("학생%d의 %s 점수를 입력하세요: " % (i+1, info[j]), end="")
        data[j] = int(input())
    
    student_data.append(sum(data))

for i in range(account):
    print("학생%d => 총점 : %d, 평균 : %.2f" % (i+1, student_data[i], student_data[i]/3))