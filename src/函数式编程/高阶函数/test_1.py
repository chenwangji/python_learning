# 列表首字母大写
def normalize(names):
    def myCapitalize(name):
        name = name.capitalize()
        return name
    return list(map(myCapitalize, names))

print(normalize(['adam', 'LISA', 'barT']))

# 求积
from functools import reduce
def prod(myList):
    return reduce(lambda x, y: x * y, myList)

print(prod([1, 2, 3]))

# 将字符串转为浮点数
def str2float(myStr):
    def str2int(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]
    def parseInt(str1):
        return reduce(lambda x, y: x * 10 + y, map(str2int, str1))
    def parseFloat(str2):
        return reduce(lambda x, y: x / 10 + y / 100, map(str2int, str2))
    total = 0
    myList = myStr.split('.')
    if len(myList) > 1:
        return parseInt(myList[0]) + parseFloat(myList[1])
    return parseInt(myList[0])

print(str2float('123.45'))
