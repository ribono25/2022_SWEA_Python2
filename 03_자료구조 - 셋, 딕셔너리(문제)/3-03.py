# 3-03.py

product_dict={
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000
}

sorted_dict = sorted(product_dict.items(), key = lambda x : x[1], reverse = True)

for key, value in sorted_dict:
    print(f'{key}: {value}')