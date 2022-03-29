# 4-03.py

data = input()

protocol_idx = data.find('://')
protocol = data[0:protocol_idx]

print(f'protocol: {protocol}')

host_idx = data.find('/', protocol_idx+3)
host = data[protocol_idx+3:host_idx]

print(f'host: {host}')
print(f'others: {data[host_idx+1:]}')