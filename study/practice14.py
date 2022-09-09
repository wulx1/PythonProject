'''
Python - pydantic（1） 入门介绍与 Models 的简单使用
'''
import random
import string

import pydantic
# from pydantic import BaseModel
# print(pydantic.compiled)
# class User(BaseModel):
#     id:int
#     name = "wulx"
# user = User(id='123')
# print(user.id, type(user.id))
# print(user.name, type(user.name))
# print(user.dict())
# print(dict(user))
#
# user.id = 321
# print(user.id)
# print(user.json())
# print(user.schema())
'''
Python - random 库的详细使用
random.randrange(stop)
random.randrange(start, stop[, step])
start：起始数字，包含（取得到 start 这个值）
stop：末尾数字，不包含（取不到 stop 这个值）
step：步长
'''
#randrange函数的使用
# for i in range(5):
#     print(random.randrange(10,20,3)

#randint函数的使用
# for j in range(5):
#     print(random.randint(1,6))
# #返回浮点数
# #返回 [0.0, 1.0) 范围内的下一个随机浮点数
# for i in range(5):
#     #print(random.random())
#     print(random.random()*10)
#
'''
random.uniform(a, b)
语法格式
返回一个随机浮点数 N
当 a <= b 时，a <= N <= b
当 b < a 时， b <= N <= a
'''
# for i in range(5):

'''
传递列表作为参数
random.choice
语法格式
从非空序列 seq 返回一个随机元素
如果 seq 为空，会抛出 IndexError
random.choice(seq)#seq非空序列
'''
# #数字数组
# print(random.choice([1,2,3,4,5,6]))
# #字母数组
# print(random.choice(["a","b","c","d"]))
# #字母元组
# print(random.choice(("a","b","c")))
# #字符串
# print(random.choice("abcd"))
# #string 模块返回的大小写字母字符串
# print(random.choice(string.ascii_letters))
# #string模块返回的数字字符串
# print(random.choice(string.digits))
# #string模块返回的大小写字符串+数字字符串
# print(random.choice(string.digits+string.ascii_letters))

'''
random.choices
语法格式
populaiton：序列
weights：普通权重
cum_weights：累加权重
k：选择次数
weights 和 cum_weights 不能同时传，只能选择一个来传
random.choices(population, weights=None, *, cum_weights=None, k=1) 
看的迷迷糊糊啥意思。。？来看栗子。。
'''
a = [1,2,3,4,5]
print(random.choices(a,k=5))
print(random.choices(a,weights=[0,0,1,0,0],k =5))
print(random.choices(a,weights=[0,0.5,1,2,0],k =5))
print(random.choices(a,cum_weights=[1,1,1,1,1],k= 5))
print(random.choices(a,cum_weights=[1,3,3,3,3],k= 5))

'''
random.shuffle
语法格式
将序列 x 随机打乱位置
只能是列表[]，元组、字符串会报错哦
random 暂时没找到有什么用，可以忽略
random.shuffle(x[, random])
'''
# a = ["a","b","c"]
# random.shuffle(a)
# print(a)
# b = [1,2,3,4,5]
# random.shuffle(b)
# print(b)
# c = "string"
# random.shuffle(c)
# print(c)

'''
random.sample
语法格式
从 population 中取 k 个元素，组成新的列表并返回
每次取元素都是不重复的，所以 population 的长度必须 ≥ k，否则会报错
random.sample(population, k)
'''
print(random.sample(a,3))





