def is_odd(n):
    return n % 2 == 1
print(filter(is_odd, range(1, 11))) # <filter object at 0x000000000117C4A8>
print(list(filter(is_odd, range(1, 11)))) # [1, 3, 5, 7, 9]

def not_empty(s):
    return s and s.strip()
result = list(filter(not_empty, ['A', 'B', None, ' ', '']))
print(result) # ['A', 'B']

# 用埃氏算法求素数
# 所有奇数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
# 筛选函数
def _not_divisable(n):
    return lambda x: x % n > 0
# 定义一个生成器，不断生成素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisable(n), it)  # 构造新序列

# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 筛选回数
def is_palindrome(n):
    strNum = str(n)
    flag = True
    for key in range(0, len(strNum) // 2 + 1):
        if strNum[key] != strNum[-(key + 1)]:
            flag = False
            break
    return flag

print(list(filter(is_palindrome, range(1, 1000))))