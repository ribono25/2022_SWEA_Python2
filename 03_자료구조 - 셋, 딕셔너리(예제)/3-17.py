# 리스트, 딕셔너리 객체를 활용하여 총점과 평균 구하기

# 3-17.py

number = int(input("총 학생 수를 입력하세요: "))

student_dict = {}
score_list = [0, 0, 0]

info = ['국어', '수학', '영어']
for num in range(number):
    name = input("학생의 이름을 입력하세요: ")

    sum = 0
    for var in range(3):
        score = int(input("{0} 학생의 {1} 점수를 입력하세요: ".format(name, info[var])))
        sum += score

        student_dict[name] = sum
        score_list[var] += score

for key, value in student_dict.items():
    print("{0} => 총점: {1}, 평균: {2:.2f}".format(key, value, value/3))

for idx, item in enumerate(score_list):
    print("{0} => 총점: {1}, 평균: {2:.2f}".format(info[idx], item, item/2))