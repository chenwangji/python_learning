# names = ['a', 'b', 'c']
# for name in names:
#     print(name)

# # 累加 计算1-10
# sum = 0
# myNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in myNums:
#     sum += num
# print(sum)

# 累加 计算1-100 可以通过range()
# sum = 0
# myNums = list(range(101))
# for num in myNums:
#     sum += num
# print(sum)

# # continue
# # 打印奇数
# myNums = list(range(101))
# for num in myNums:
#     if num % 2 == 0:
#         continue
#     print(num)

# # break
# myNums = list(range(101))
# for num in myNums:
#     if num > 10:
#         break
#     print(num)

# while
# 计算100内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)