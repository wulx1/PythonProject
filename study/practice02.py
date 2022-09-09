#list = [1, -1, 2, -2, 3, -3]


# def positive():
#     for itme in list:
#         if itme >0:
#             print(itme)
#
# def nagetive():
#     for item in list:
#         if item <0:
#             print(item)

# def positive(x):
#     return x>0
#
# def nagetive(x):
#     return x<0
#
# def test(list,fun):
#     for item in list:
#         if fun(item):
#             print(item)

def test1(list, fun):
    for item in list:
        if fun(item):
            print(item)

#map函数的写法：
list=[1,2,3]
def test2(x):
    x = x+5
    return x
list1 = map(test2,list)
for i in list1:
    print(i)

#lambda写法：
list2 = map(lambda x:x+5,list)
for i in list2:
    print(i)
# if __name__ == '__main__':
    # test1(list, lambda x: x > 0)
    # test1(list, lambda x: x < 0)
