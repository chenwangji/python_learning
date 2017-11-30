from collections import Iterable
myList = [x for x in range(1, 11)]
myGenerator = (x for x in range(1, 11)) # 生成器
myDict = {
    'a': 1,
    'b': 2
}
myStr = '123'
print(isinstance(myList, Iterable)) # True
print(isinstance(myGenerator, Iterable)) # True
print(isinstance(myDict, Iterable)) # True
print(isinstance(myStr, Iterable)) # True

# 生成器除了可以用for循环，还可以被next()函数不断调用，并返回下一个值，直到最后抛出stopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可以用isinstance()判断一个对象是否为Iterator
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator)) # True
print(isinstance('12321', Iterator)) # False

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator)) # True
