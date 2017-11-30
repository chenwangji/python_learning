from functools import reduce
def add(x, y):
    return x + y
result = reduce(add, list(range(1, 11)))
print(result) # 55

# 将[1, 2, 3, 4] 转化为1234
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 2, 3, 4])) # 1234

def reduceFn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]

print(reduce(reduceFn, map(char2num, '13123'))) # 13123

# 整理
def char2int(myStr):
    def reduceFn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]
    return reduce(reduceFn, map(char2num, myStr))

print(char2int('312321'))

# 用lambda函数进一步简化
def char2int_lambda(myStr):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, myStr))

print(char2int_lambda('13123123'))







