# 生成 1-10
list1 = list(range(1, 11))
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成 [1x1, 2x2, 3x3, ..., 10x10]
# 循环
list2 = []
for x in range(1, 11):
    list2.append(x * x)
print(list2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表生成式
print([x * x for x in range(1, 11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 可以增加条件
print([x * x for x in range(1, 11) if x % 2 == 0]) # [4, 16, 36, 64, 100]
# 循环嵌套
print([m + n for m in 'ABC' for n in 'abc']) # ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']
# dict 的key,value
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
print([k + '-' + str(v) for k, v in d.items()]) # ['a-1', 'b-2', 'c-3']

# 将list中的大写转为小写(list中含有非str)
myList = ['A', 'B', 12]
lowerList = [isinstance(s, str) and s.lower() or s for s in myList]
print(lowerList) # # 生成 1-10
list1 = list(range(1, 11))
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成 [1x1, 2x2, 3x3, ..., 10x10]
# 循环
list2 = []
for x in range(1, 11):
    list2.append(x * x)
print(list2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 列表生成式
print([x * x for x in range(1, 11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 可以增加条件
print([x * x for x in range(1, 11) if x % 2 == 0]) # [4, 16, 36, 64, 100]
# 循环嵌套
print([m + n for m in 'ABC' for n in 'abc']) # ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']
# dict 的key,value
d = {
    'a': 1,
    'b': 2,
    'c': 3
}
print([k + '-' + str(v) for k, v in d.items()]) # ['a-1', 'b-2', 'c-3']

# 将list中的大写转为小写(list中含有非str)
myList = ['A', 'B', 12]
lowerList = [isinstance(s, str) and s.lower() or s for s in myList]
print(lowerList) # ['a', 'b', 12]

