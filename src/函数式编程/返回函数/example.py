# 常规求和函数
def calc_sum(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# 返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f) # <function lazy_sum.<locals>.sum at 0x000000000118E950>
print(f()) # 25

# 闭包
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3()) # 1 4 9

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    count = 0
    def add():     
        nonlocal count # 在 Python 中，内层函数对外层作用域中的变量仅有只读访问权限！而 nonlocal 可以使我们自由地操作外层作用域中的变量！
        count += 1
        return count
    return add
fn = createCounter()
print(fn(), fn()) # 1 2


