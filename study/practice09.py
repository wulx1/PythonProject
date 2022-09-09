class Car:
    def __init__(self,name):
        self.name  = name

    def driver(self):
        print("正在开车")

    def stop(self):
        print("正在停车")

class Truck(Car):
    def driver(self):
        print(f"{self.name}准备开车上路了!")

    def stop(self):
        print(f"{self.name}正在飘逸停车")

class Baoma(Car):
    def driver(self):
        print(f"{self.name}准备开车上路了")

    def stop(self):
        print(f"{self.name}正在飘逸停车")

class Person:
    def __init__(self,name):
        self.name = name

    def driverCar(self,car):
        print(f"{self.name}准备开车上路")
        car .driver()

    def stopCar(self,car):
        print(f"{self.name}准备靠边停车")
        car.stop()

person = Person("wlx")
truck = Truck("卡车")
baoma = Baoma("baoma")
person.driverCar(truck)
person.stopCar(baoma)

'''
前言
主要是针对静态方法、类方法、实例方法、类属性、实例属性的混合实战
需求
设计一个 Game 类

属性

定义一个类属性 top_score 记录游戏的历史最高分，这个属性很明显只跟游戏有关，跟实例对象无关，所以定义为类属性
定义一个实例属性 player_name 记录当前游戏的玩家姓名
方法

静态方法：showHelp，显示游戏帮助信息，这个方法不需要访问类属性，也不需要访问实例属性，所以可以定义为静态方法
类方法：showTopScore，显示历史最高分，只需要访问类属性，所以定义为类方法
实例方法：startGame，开始游戏，由实例对象调用
主程序

查看帮助信息
查看历史最高分
创建游戏对象，开始游戏
更新历史最高分
'''
class Game:
    __top_score = 0
    def __init__(self,player_name):
        self.__player_name = player_name

    @staticmethod
    def show_help():
        print("游戏帮助---help")

    @classmethod
    def ShowTopScore(cls):
        return cls.__top_score

    @classmethod
    def SetTopScore(cls,score):
        cls.__top_score = score

    def startGame(self,score):
        #1.玩游戏
        print(f"{self.__player_name}开始玩游戏了...")
        if score > self.ShowTopScore():
            self.SetTopScore(score)

player1 = Game("wlx")
player1.show_help()
print(player1.ShowTopScore())
player1.startGame(100)
print(player1.ShowTopScore())


