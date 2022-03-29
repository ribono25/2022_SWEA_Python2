# 4-01.py

data = input()

reverse_datalist = [data[i] for i in range(-1, -len(data)-1, -1)]
reverse_data = ''.join(reverse_datalist)

if data == reverse_data:
    print(f'{data}')
    print('입력하신 단어는 회문(Palindrome)입니다.')
else:
    print('입력하신 단어는 회문(Palindrome)이 아닙니다.')