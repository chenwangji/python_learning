# 位置参数
# def power(x, n):
#     s = 1
#     while n > 0:
#         n -= 1
#         s *= x
#     return s
# result = power(2, 3)
# print(result)

# # 默认参数
# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# result = power(3)
# print(result) # 9

# # 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n * n
#     return sum
# result2 = calc(1, 2)
# print(result2) # 5
# # 如果要传的是list或者tuple,可以简化
# nums = [1, 2]
# result3 = calc(*nums)
# print(result3) # 5

### 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('wangji', 25, gender='male', height='175cm') # name: wangji age: 25 other: {'gender': 'male', 'height': '175cm'}