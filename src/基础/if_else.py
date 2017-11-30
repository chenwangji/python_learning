
# if...else
# age = 20
# if age >= 18:
#     print('your age is %s' % age)
#     print('adult')
# else:
#     print('your age is %s' % age)
#     print('teenager')

#if...elif...else
age = 10
if age >= 18:
    print('your age is %s' % age)
    print('adult')
elif age > 12:
    print('teenager')
else:
    print('your age is %s' % age)
    print('kid')

# 再议input
myInput = input('请输入数字')
if int(myInput) > 10:
    print(myInput)