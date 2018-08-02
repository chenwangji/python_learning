# # 创建生成器
# g = (x * x for x in range(1, 11))
# item1 = next(g)
# item2 = next(g)
# item3 = next(g)
# item4 = next(g)
# item5 = next(g)
# item6 = next(g)
# item7 = next(g)
# item8 = next(g)
# item9 = next(g)
# item10 = next(g)
# print(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10) # 1 4 9 16 25 36 49 64 81 100
# 迭代generator对象
# g = (x * x for x in range(1, 11))
# for n in g:
#     print(n)

# # 斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b 
#         n += 1
#     return 'done'
# fib(10)
# # 这里的赋值实际上是：
# t = (0, 0, 1)
# n = t[0]
# a = t[1]
# b = t[2]

# # yield
# def odd():
#     print('step 1')
#     yield(1)
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# o = odd()
# next(o)
# next(o)
# next(o)
# next(o)

def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break
