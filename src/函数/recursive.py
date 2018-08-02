# 递归计算10的阶乘
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n
result = fact(10)
print(result)