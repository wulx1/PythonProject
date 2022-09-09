'''
需求：士兵突进
士兵许三多有一把 AK47
士兵可以开火
枪能够发射子弹
枪装填子弹，可以增加子弹数量

需求分析：
士兵是一个类，枪是一个类
士兵的姓名是一个属性，拿开火是士兵的一个行为方法
枪的子弹是一个属性，抢可以发射是士兵的一个行为

'''

class Gun:
    def __init__(self,name):
        self.__name = name
        self.__bullet_count = 0

    def __str__(self):
        return f'枪的名字：{self.__name},枪的子弹数量为：{self.__bullet_count}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def bullet_count(self):
        return self.__bullet_count

    @bullet_count.setter
    def bullrt_count(self,count):
        self.__bullet_count += count

    def shoot(self,):
        if self.__bullet_count <= 0:
            print(f"{self.__name}里没有子弹，请先装弹")
        else:
            self.__bullet_count -= 1
            print(f"{self.__name}正在发射，")

class solider:
    def __init__(self,name):
        self.__name = name
        self.__gun = None

    def __str__(self):
        return f'士兵:{self.__name},拿着一把{self.__gun.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def gun(self):
        return self.__gun

    @gun.setter
    def gun(self,gun):
        self.__gun = gun

    def fire(self):
        if self.__gun is None:
            print(f"{self.__name}没有枪，不能发射，请先装备枪！")

        else:
            self.__gun.bullrt_count += 10
            self.__gun.shoot()






# 声明一个枪
ak47 = Gun("ak47")
print(ak47)

# 声明一个士兵
xusanduo = solider("许三多")
# 给士兵带上 AK47！
xusanduo.gun = ak47
# 开火！
xusanduo.fire()

print(xusanduo)




