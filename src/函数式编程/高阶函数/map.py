def f(x):
    return x * x
r = map(f, list(range(1, 12)))
print(r) # <map object at 0x0000000000A9C588>
print(list(r)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]

# 转成字符串
result = list(map(str, list(range(1, 11))))
print(result) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

