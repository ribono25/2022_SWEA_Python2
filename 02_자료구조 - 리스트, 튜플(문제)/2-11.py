# 연습문제 11

# 2-11.py

def fibo(var):
    if var == 1 or var == 2:
        return 1
    
    return fibo(var - 1) + fibo(var - 2)

fibo_list = [fibo(i) for i in range(1, 11)]
print(fibo_list)