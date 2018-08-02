# 函数的可以接受函数作为参数，这样的函数称为高阶函数
def add(x, y, f):
    return f(x) + f(y)
result = add(10, -20, abs)
print(result)