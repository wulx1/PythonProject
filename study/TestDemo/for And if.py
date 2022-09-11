# -*- coding:utf-8 -*-
for i in range(1,10):
    print(i , "",end="")
print()
dict1 = {"wulx":12,"wulx2":13}
for i in dict1:
    print(i)
for key in dict1.items():
    print(key)
for i in dict1.values():
    print(i)

#当我们需要判断 sum 大于 1000 的时候，不在相加时，可以用到 break ，退出整个循环
count = 1
sum = 0
while(count<100):
    sum = sum + count
    if sum>1000:
        break
    count = count +1
print(sum)

