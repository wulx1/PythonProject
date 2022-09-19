# -*- coding:utf-8 -*-
for i in range(1, 10):
    print(i, "", end="")
print()
dict1 = {"wulx": 12, "wulx2": 13}
for i in dict1:
    print(i)
for key in dict1.items():
    print(key)
for i in dict1.values():
    print(i)

# 当我们需要判断 sum 大于 1000 的时候，不在相加时，可以用到 break ，退出整个循环
# count = 1
# sum = 0
# sum_list = []
# count_list = []
# while(count<100):
#     sum = sum + count
#     if sum>1000:
#         break
#     count = count +1
#     sum_list.append(sum)
#     count_list.append(count)
# print(sum)
# print(sum_list)
# print(count_list)
# print(count)
'''
有时候，我们只想统计 1 到 100 之间的奇数和，那么也就是说当 count 是偶数，也就是双数的时候，我们需要跳出当次的循环，不想加，这时候可以用到 break
'''
num = 1
result = 0
while (num < 100):
    if num % 2 == 0:
        num = num + 1
        continue
    result = num + result
    num = num + 1
print(result)

'''计算1到100的奇数和and偶数和'''
count = 0
result1 = 0
result2 = 0
while count <= 100:
    if count % 2 == 0:
        result1 = result1 + count
    else:
        result2 = result2 + count
    count += 1
print(result1, result2)


def ma():
    for num in range(10, 20):  # 迭代 10 到 20 之间的数字
        for i in range(2, num):  # 根据因子迭代
            if num % i == 0:  # 确定第一个因子
                j = num / i  # 计算第二个因子
                print('%d 是一个合数' % num)
                break  # 跳出当前循环
        else:  # 循环的 else 部分
            print('%d 是一个质数' % num)


ma()

'''条件语句和循环语句综合实例'''
# 1、打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i * j} ", end="")
    print()
    print("测试")

# '''判断年份是不上闰年'''
# year = int(input("请输入年份:"))
# if year % 4 == 0 and year % 400 == 0:
#     print(year,"是闰年")
# else:
#     print(year , "不是闰年")

list1 = list(range(1,21))
print(list1)
list2 = [x + x for x  in range(1,11) if x %2 == 0]
list3 = ()
print(list2)
for i in reversed(list1):
    print(i,end=" ")
