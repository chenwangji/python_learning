# 对数字类型数组的排序
result = sorted([3, -1, 0, 12, 4])
print(result) # [-1, 0, 3, 4, 12]

# key函数自定义排序
result2 = sorted([3, -1, 1, 0, -10, -2], key=abs)
print(result2) # [0, -1, 1, -2, 3, -10]

# 字符串的排序，默认根据ascii码
result3 = sorted(['wfs', 'sswfw', 'Tom', 'asf'])
print(result3) # ['Tom', 'asf', 'sswfw', 'wfs']

# 自定义函数，忽略大小写
result4 = sorted(['wfs', 'sswfw', 'Tom', 'asf'], key = str.lower)
print(result4) # ['asf', 'sswfw', 'Tom', 'wfs']

# reverse = True 反转，默认False
result5 = sorted(['wfs', 'sswfw', 'Tom', 'asf'], key = str.lower, reverse = True)
print(result5) # ['wfs', 'Tom', 'sswfw', 'asf']

# 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(item):
    return item[0].lower()
def by_score(item):
    return -int(item[1])

result6 = sorted(L, key = by_name)
print(result6) # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

result7 = sorted(L, key = by_score)
print(result7) # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]

