# 라이브러리로 사용할 목적의 모듈

# 1-08.py

import module_08_1, module_08_2 # 모듈로 실행

op1, op2 = 2, 3

result = module_08_1.plus(op1, op2)
print("plus(%d, %d) => %d" % (op1, op2, result))

result = module_08_1.minus(op1, op2)
print("minus(%d, %d) => %d" % (op1, op2, result))

result = module_08_2.multiply(op1, op2)
print("multiply(%d, %d) => %d" % (op1, op2, result))

result = module_08_2.divide(op1, op2)
print("divide(%d, %d) => %.2f" % (op1, op2, result))