'''计算列表数字的和'''
list1 = list(range(1,6))
list2 = list1.copy()
print(list2)
print(list1)
list2.append(8)
print(list2)
list2.reverse()
print(list2)
result = 0

for i in list1:
    result = result+i
print(result)
result1 = 0
for i in list2:
    result1 +=i
print(result1)

begin = int(input("请输入要计算的开始区间的值:"))
end = int(input("请输入要计算结束区间的值:"))
list3 = []
for i in range(begin,end+1):
    if i %2 ==0:
        list3.append(i)
print(list3)