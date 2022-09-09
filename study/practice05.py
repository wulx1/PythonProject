'''
 了解cls参数的作用
 面向对象编程
 类方法的运用
# '''
# class test:
#     sum = 0
#     @classmethod
#     def class_fun(cls):
#         print("class_fun cls 对象的id",id(cls))
#         cls.sum +=1
#         print("类属性sum:",cls.sum)
#
#     @classmethod
#     def class_fun2(cls):
#         print("class_fun2 cls 对象的ID",id(cls))
#         cls.sum +=1
#         print("类属性sum:",cls.sum)
# #运行结果可看出，cls指的是同一个类对象
# test.class_fun()
# test.class_fun2()

#类方法调用实例方法
class test:
    sum =0
    def __init__(self,sum):
        self.sum=sum

    def test(self):
        print("self id is",id(self))
        print("self 对象num的值为",self.sum)

    @classmethod
    def fun(cls):
        print("cls id is",id(cls))
        print("cls 对象num的值为",cls.sum)
        cls.test(cls)

# test.fun()
# print()
# print("实例对象调用类方法")
# t =test(2)
# t.fun()

#实例方法调用类属性
class test1:
    name ="我是类属性"

    def __init__(self,name):
        self.name=name

    def print_name(self):
        print(self.name)
        print(test1.name)
t1 =test1("wlx")
t1.print_name()
'''
扩展思考题！
一个方法内部既需要访问实例属性，又需要访问类属性，应该定义为什么方法？
答案：实例方法，因为可以通过 类对象.类属性 来访问，但在类方法中无法访问实例属性
代码栗子直接看上面一个就是啦！

'''

#静态方法实际例子
# class test2:
#
#     @staticmethod
#     def test(name,age):
#         print(name,age)
#
# test2.test("wlx",23)
# t = test2()
# t.test("wlx",22)
#
# #print实例对象，看是那个类的创建的对象
# class test3:
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
# t3 = test3('wlx')
# print(t3)

# 重写 __repr__ 方法
# class test4:
#     def __init__(self):
#         self.name ='wlx'
#         self.age= 22
#
#     def __repr__(self):
#         return self.name,self.age
#
# t5 = test4()
# print(t5)

'''
私有属性、私有方法
'''
class test1:
    def __init__(self):
        self.__name = "wlx"
        self.__age = 22

    def print_name(self):
        print(self.__name)

    def __print_age(self):
        print(self.__age)

t1 =test1()
t1.print_name()
# #直接调用私有方法和私有属性会报错
# print(t1.__name)
# t1.print_age()
#

class test2:
    __sum =0
    def __init__(self,name,age):
        self.__name =name
        self.__age = age

    def __test(self):
        print("name is"+self.__name)
'''
无论是类对象还是实例对象，都可以通过 ._类名__名称 来调用私有属性、方法，这算是一种间接调用
'''
print(test2._test2__sum)
t2 = test2("wlx",22)
print(t2._test2__name)
t2._test2__test()






