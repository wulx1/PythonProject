'''
需求
小明和小美都爱跑步
小明体重 75 公斤
小美体重 45 公斤
每次跑步会减肥 0.5 公斤
每次吃东西体重增加 1 公斤

需求分析：
小明、小美都是一个具体的对象，他们都是人，所以应该抽象成人类
小明、小美是具体的对象的姓名，而体重是另一个属性，所以有两个属性
跑步、吃东西都是一种行为，所以也有两个方法
'''
class Person:
    #构造方法
    def __init__(self,name,weight):
        self.name =name
        self.weight = weight

    def __str__(self):
        return f"{self.name}目前基础信息：名字：{self.name}  体重：{self.weight} 很爱跑步"

    def run(self):
        print(f"{self.name}在跑步，体重减少0.5公斤")
        self.weight -= 0.5

    def eat(self):
        print(f"{self.name}在吃东西，体重加1公斤")
        self.weight += 1

xiaoming = Person("小明",65)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美",45)
xiaomei.run()
xiaomei.run()
print(xiaomei)




'''
需求
房子（House）有户型、总面积、家具名称列表；新房子没有任何的家具 
家具（HouseItem）有名字、占地面积
席梦思（bed） 占地 4 平米
衣柜（bed） 占地 2 平米
餐桌（bed） 占地 1.5 平米
将以上三个家具添加到房子中
打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

需求分析
家具有两个属性，房子表面上有三个属性
新房子没有任何的家具，代表构造方法不需要给家具名称列表属性初始化赋值
但房子其实还有一个特殊属性，剩余面积，它的初始值应该和总面积相同
房子添加家具后，剩余面积应该减掉家具的占地面积
席梦思、衣柜、餐桌都是一个具体的对象，都是家具类的实例对象
 

思考：房子、家具两个类应该先开发哪个类
家具类
因为家具类简单，只有两个方法，且没有行为
房子要使用到家具，被依赖的类，通常应该先开发，可以避免在开发主类过程中，要中途插入开发被依赖的类
'''


class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"家具名称：{self.name}  家具占地面积为：{self.area}"

class House:
    def __init__(self,type,area):
        self.house_type = type
        self.area = area
        self.free_area = area
        self.Item_list = []


    def __str__(self):
        return f"户型名称：{self.house_type}\n" \
               f"房子占地面积：{self.area}\n" \
               f"房子剩余面积：{self.free_area}\n" \
               f"家具列表：{self.Item_list}\n"

    def add_item(self,item):
        if item.area > self.free_area:
            print("剩余面积不足于添加",item.name)
            return
        self.Item_list.append(item.name)
        self.free_area -= item.area

bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",3)
table = HouseItem("桌子",2)
print(bed)

wlx =House("复试",120)
print(wlx)
wlx.add_item(bed)
wlx.add_item(chest)
wlx.add_item(table)
print(wlx)

# class test:
#     def __init__(self,name):
#         self.name = name
#
# t = test("wlx")
# print(t.name)
#
# t.name = 'wlx123'
# print(t.name)

# class test1:
#     def __init__(self,name):
#         self.name = name
#
#     def setName(self,name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
# t1 = test1("wlx")
# print(t1.name)
# print(t1.getName())
# t1.setName("wlx123")
# print(t1.getName())

class test2:
    def __init__(self,name):
        self.__name = name

    def setName(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def delname(self):
        self__name = 'xxx'

class test3:
    def __init__(self,name):
        self.name =name

    def __str__(self):
        return f'这是名字为{self.name}的实例对象'

    @property
    def name_fun(self):
        return self.name

    @name_fun.setter
    def name_fun(self,name):
        self.name = name

    @name_fun.deleter
    def name_fun(self):
        print("删除了name")

wlx = test3("wlx")
print(wlx)
print(wlx.name)
wlx.name = "123"
print(wlx.name)
del wlx.name_fun
print(wlx.name)