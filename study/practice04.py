'''
 了解self参数的作用
 面向对象编程
 实例化方法运用
# '''
#
#
# class test:
#     def __init__(self):
#         self.name = 'wlx'
#
#     def test(self):
#         print(self.name)
#
#
# t = test()
# t.test()
#
# # class test:
# #     def __init__(self):
# #         self.name = "小菠萝"
# #
# #     def test(self):
# #         print(self.name)
# #
# #
# # t = test()
# # t.test()
#
# '''
# 设计一个类Person，生成若干实例，在终端输出如下信息
#
# 小明，10岁，男，上山去砍柴
#
# 小明，10岁，男，开车去东北
#
# 小明，10岁，男，最爱大保健
#
# 老李，90岁，男，上山去砍柴
#
# 老李，90岁，男，开车去东北
#
# 老李，90岁，男，最爱大保健'''
# # class Persons:
# #     def __init__(self):
# #         self.name ='小明'
# #         self.age ='10'
# #         self.sex = '男'
# #         self.doying = '上山去砍柴'
# #
# #     def printMassage(self):
# #         print(self.name,self.age,self.sex,self.doying)
# #
# # xiaoming = Persons()
# # xiaoming.printMassage()
#
# class person:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex =sex
# #获取对象的属性
#     def getMassage(self):
#         return self.name,self.age,self.sex
# #行为方法
#     def doing(self,doing):
#         print(*self.getMassage(),doing)
#
# xiaoming = person('小明',20,'男')
# xiaoming.doing("上山去砍柴")
# xiaoming.doing('开车去东北')
# xiaoming.doing('最爱大保健')
# print()
# laoli =person('老李',40,'男')
# laoli.doing("上山去砍菜")
# laoli.doing("开车去东北")
# laoli.doing("最爱大保健")
#
# #实例属性的栗子
# class test:
#     def __init__(self):
#         # 在方法内部，通过 self.name 的方式定义的变量就是实例变量
#         self.name = 'wlx python 学习笔记 '
#         self.age = 22
#
#     # 下面定义了一个 say 实例方法
#     def say(self):
#         self.sex = '男'
# #实例化对象
# t =test()
# #t.sex直接通过实例对象去访问方法属性会直接报错
# print("姓名："+t.name ,"年龄: "+ str(t.age),)
# t.say()
# print(t.sex)
# '''
# 重点：__init__ 会在实例化对象的时候自动调用，因此 blog 创建成功就有 name、add 两个实例属性
# 调用 say() 方法之后才有第三个实例属性 age
# '''
#
# class ObjectTest:
#     sum=0
#     st1 = ObjectTest()
#     test2 = ObjectTest()
#     test3 = ObjectTest()
#     print(ObjectTest.sum)
#     test1.print()
#
#     '''
#     实例属性、类属性出现同名的现象
#     '''
#
#     class test1:
#         # 只有一个类变量
#         name = 'wlx'
#
#     # 实例化一个对象
#     t = test1()
#     # 打印实例属性name的值，因为实例对象没有name，所以会继续去查找class类的name的值
#     print(t.name)
#     # 打印类的属性name
#     print(test1.name)
#     # 重新赋值给实例对象name，age
#     t.name = 'wulongxing'
#     t.age = 22
#     # 由于实例属性优先级比类属性高，所以优先打印实例对象属性name，age，屏蔽掉类属性的值
#     print(t.age, t.name)
#     # 仍然打印类属性的值
#     print(test1.name)
#
#     def __init__(self):
#         self.name ='wlx'
#         self.age =20
#         ObjectTest.sum +=1
#
#     def print(self):
#         print(self.name,self.age)
#
'''
实例方法列子
'''
class test:
    def __init__(self,name,age):
        print("实例化对象时候，自动调用构造方法，获取name，age")
        self.name=name
        self.age = age

    def test01(self):
        print("一个实例方法，需要通过对象来调用")
        print("my name is :"+self.name,"    " "my age is : "+self.age)

t = test("wlx","22")
t.test01()
test.test01(t)
