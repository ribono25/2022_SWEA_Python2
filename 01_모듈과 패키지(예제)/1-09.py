# 패키지 사용

# 1-09.py

from package_09 import module_09_1, module_09_2 # from 패키지 import 모듈
# from package_09 import # 모든 모듈 로딩

op1, op2 = 2, 3

result = module_09_1.plus(op1, op2)
print("plus(%d, %d) => %d" % (op1, op2, result))

result = module_09_1.minus(op1, op2)
print("minus(%d, %d) => %d" % (op1, op2, result))

result = module_09_2.multiply(op1, op2)
print("multiply(%d, %d) => %d" % (op1, op2, result))

result = module_09_2.divide(op1, op2)
print("divide(%d, %d) => %.2f" % (op1, op2, result))