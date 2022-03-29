# 공백 제거 4-10.py

data_str = "   홍  길동   "
data_str = data_str.lstrip(" ")
print(f"'{data_str}' : ({len(data_str)})")

data_str = "___홍  길동___  "
data_str = data_str.rstrip("_ ")
print(f"'{data_str}' : ({len(data_str)})")

data_str = " 0?홍  길동 _#    "
data_str = data_str.strip(" 0?_#")
print(f"'{data_str}' : ({len(data_str)})")