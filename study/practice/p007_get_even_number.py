'''计算某个区间所有的偶数'''
begin = int(input("输入开始区间的值:"))
end = int(input("输入结束区间的值:"))
list = []
for i in range(begin,end+1):
    if i % 2 == 0:
        list.append(i)
print(list)