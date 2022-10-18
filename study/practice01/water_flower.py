'''
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）
'''
import math

lists = []
for i in range(101, 1000):
    i = str(i)
    i1, i2, i3 = int(i[0]), int(i[1]), int(i[2])
    if int(i) == int(math.pow(i1, 3) + math.pow(i2, 3) + math.pow(i3, 3)):
        lists.append(i)

print(lists)

