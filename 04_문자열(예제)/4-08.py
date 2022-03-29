# 문자열의 삽입 4-08.py

data_str = "가나다라마바사아자차카타파하"
comma_space = ", "

output = comma_space.join(data_str)
print(f"{type(output)}: {output}")