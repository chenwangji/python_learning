# dict迭代
# 默认迭代key
d = {
    'a': 1, 
    'b': 2,
    'c': 3
}
for key in d: 
    print(key)
# 迭代value
for value in d.values():
    print(value)    
# 迭代key和value
for (k, v) in d.items():
    print(k, v)

# 迭代字符串
for ch in 'ABC':
    print(ch)

# Iterable对象
from collections import Iterable 
print(isinstance('abc', Iterable)) # True
print(isinstance([1, 2, 3], Iterable)) # True
print(isinstance(123, Iterable)) # False

# enumerate将list变为索引-元素对
for i, value in enumerate(['A', 'B', 'D']):
    print(i, value)

# 同时引用两个变量
for x, y in [(1, 1), (2, 4), (3,11)]:
    print(x + y)