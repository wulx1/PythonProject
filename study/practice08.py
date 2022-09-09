'''
继承，重写父类方法

'''

class Animal1:
    def eat(self):
        print("吃东西...")

    def drink(self):
        print("喝水...")

    def run(self):
        print("跑步...")


class Dog(Animal1):
    def wang(self):
        print("汪汪叫...")


class Chai(Dog):
    def shake(self):
        print("小柴柴摇尾巴...")

    def wang(self):
        # 1、针对子类特有的需求，编写子类独有的代码实现
        print("柴犬小声的汪汪叫")

        # 2、调用父类方法
        super().wang()

        # 3、子类的其他代码块
        print("柴犬真可爱")


chai = Chai()
chai.wang()

class Person:
    def __init__(self,name):
        self.name = name

    def print(self):
        print(self.name)

class goodPerson(Person):
    def __init__(self,name,age):
        super(goodPerson, self).__init__(name)
        self.age = age

    def print(self):
        super(goodPerson,self).print()
        print(self.age)


wlx = goodPerson("wlx",22)
wlx.print()


# class Animal:
#     def __init__(self,Animalname):
#         print(Animalname,"是一种动物")
#
# class mammal:
#     def __init__(self,mammal):
#         print(mammal,"mammal")
#         super(mammal, self).__init__(Animal)


# class A:
#     def test(self):
#         print("AAA")
#
# class B:
#     def test(self):
#         print("BBB")
#
# class C(B,A):
#     def test(self):
#         print("CCC")
#         super().test()
# c = C()
# c.test()

# class A:
#     def __init__(self):
#         print("A",end=" ")
#         super().__init__()
# class B:
#     def __init__(self):
#         print("B",end=" ")
#         super().__init__()
# class C(A,B):
#     def __init__(self):
#         print("C",end=" ")
#         A.__init__(self)
#         B.__init__(self)
# print("MOR:",[x.__name__ for  x in c.__mro__])
# C()
#



class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()


class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C", end=" ")
        B.__init__(self)
        A.__init__(self)


print("MRO:", [x.__name__ for x in C.__mro__])
C()
print(C.__mro__)

class Dog:
    def __init__(self,name):
        self.name = name

    def game(self):
        print(f'{self.name} 狗狗在玩耍')

class chaiquan(Dog):
    def game(self):
        print(f'{self.name}柴犬在疯疯癫癫玩耍')

class Person:
    def __init__(self,name):
        self.name = name

    def gamewithdog(self,dog):
        print(f'{self.name}在和{dog.name}在玩耍')
        dog.game()
dog1 = Dog("旺柴")
chai = chaiquan("柴犬")
p = Person("吴龙兴")
p.gamewithdog(dog1)
p.gamewithdog(chai)





