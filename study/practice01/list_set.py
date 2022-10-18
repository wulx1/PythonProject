'''

问题1.对列表a 中的数字从小到大排序

问题2.排序后去除重复的数字
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]

'''
#非算法方案
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
a.sort()
print(a)
a =set(a)
a = list(a)
print(a)

#算法方案，冒泡排序
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 6, 8]
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

a = set(a)
a = list(a)
print(a)