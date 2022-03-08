# module_10.py

from random import sample

def input_start():
    try:
        start_number = int(input('로또 번호의 시작 번호를 입력하세요 (기본값: 1): '))
    except Exception as ValueError:
        start_number = 1
    finally:
        return start_number
def input_end():
    try:
        end_number = int(input('로또 번호의 끝 번호를 입력하세요 (기본값: 45): '))
    except Exception as ValueError:
        end_number = 45
    finally:
        return end_number
def input_amount():
    try:
        amount = int(input('로또 공의 개수를 입력하세요 (기본값: 6): '))
    except Exception as ValueError:
        amount = 6
    finally:
        return amount

def output(start, end, am):
    data = sorted(sample(list(range(start, end+1)), k=am))
    print('행운의 로또 번호는 ', end="")
    print(', '.join(map(str, data)), end=" 입니다.")