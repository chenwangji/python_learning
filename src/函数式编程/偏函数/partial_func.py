# int()默认按10进制转化
print(int('12345')) # 12345

# 其他进制
print(int('12345', base=8)) # 5349
print(int('12345', base=16))

# 偏函数
import functools
int2 = functools.partial(int, base=2)
print(int2('100000')) # 32

# 偏函数设定的固定参数可以被覆盖
print(int2('100000', base=10)) # 100000

# 固定参数
max2 = functools.partial(max, 10)
print(max2(2, 3, 5, 8)) # 10