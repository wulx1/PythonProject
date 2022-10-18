'''从列表中移除多个元素'''
list1 = [1,2,3,4,5,6,7,8,2,3,5]
list2 = [2,3,5]
for i in list2:
    list1.remove(i)
print(list1)

list3 = list1 + list2
print(list3)
list4 = set(list3)
print(list4)
list5 = [20,10,10,10,20,30]
print(list5)
result = []
for i in list5:
    if i not in  result:
        result.append(i)
print(result)