'''
range函数
列表生成式
'''
# for i in range(5):
#     print(i)

# res = []
# for i in range(0,11):
#     res.append(i*i)
# print(res)
# #等价写法
# res = [i*i for i in range(11)]
# print(res)

# d ={"a":"1","b":"2"}
# res = []
# for k,v in d.items():
#     res.append((k,v))
# print(res)
# L = ['Hello', 'World', 'IBM', 'Apple']
# re = []
# for i in L:
#     re.append(i.lower())
# print(re)

'''
什么是生成器
若列表元素可以按照某种算法算出来，就可以在循环的过程中不断推算出后续需要用的元素，而不必创建完整的 list，从而节省大量的空间
边循环边计算的机制，叫生成器（generator）
'''
L = (x*x for x in range(10))
print(L)
print(type(L))
L1 = [i*i for i in range(10)]
print(L1)
print(type(L))
res = []
for i in L:
    res.append(i)
print(res)
