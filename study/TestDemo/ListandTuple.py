# -*- coding:utf-8 -*-
# --------------list的使用-----------------
user = ["wulx", "张三", "喜欢打游戏", 123]
print(len(user))
print(user[0])
user.append("wulongxing")
print(user)
user.insert(0, "vip")
print(user)
user.pop(0)
print(user)
user[1] = "张四"
print(user)
user.remove("wulongxing")
print(user)
user.reverse()
print(user)

# -----------tuple的使用---------------

tuple3 = ("wulx", "123", "八块腹肌", user)
tuple2 = ("wulx1", "wulx2", "wulx3")
print(tuple3)
print(type(tuple3))
tuple1 = ("wulx",)
print(tuple1)
print(type(tuple1))
print(len(tuple3))
print(tuple3 + tuple1)
print(tuple1 * 2)
if "wulx1" in tuple3:
    print(tuple3)
else:
    print("不存在")
print(max(tuple2))
print(min(tuple2))
print(tuple(user))
print(list(tuple3))

# ------------字典的使用-------------
dict1 = {"wulx": 17, "wulx2": 18, "wulx3": 19}
dict2 = {"wulx": 17, "wulx2": 18, "wulx3": 19,"wulx":22}
dict3 = {"wulx": 17, "wulx2": 18, "wulx3": 19,111:"wulx",("wulx",123):"腹肌"}
print(dict1)
print(dict1["wulx"])
dict1["wulx"] = 22
print(dict1)
dict1["wulx4"] = 30
print(dict1)
del dict1["wulx4"]
print(dict1)
dict1.clear()
print(dict1)
del dict1
print(dict2)
print(dict3)
print(len(dict3))
print(str(dict2))
print(type(dict2))
aa = dict2.copy()
print(aa)
dict2["wulx4"]=33
print(aa)
print(dict2)
bb =dict2.values()
print(bb)
print(type(bb))
print(dict2)
dict2.popitem()
print(dict2)

cc=dict2.items()
print(type(cc))
for key,vaule in cc:
    print(key,vaule)
print("dd")
print("通过git提交代码")

