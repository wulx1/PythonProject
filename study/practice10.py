'''
__call()__ 的作用
使得类实例对象可以像普通函数那样被调用
'''

from typing import Callable
class Wlx:
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(self.name)
        print(args)
        print(kwargs)

wlx = Wlx("wulongxing")
wlx(1,2,3,age = 22,sex = "boy")
print(isinstance(wlx,Callable))

'''
__new__ 方法
使用 类名() 创建对象时，Python 的解释器首先会调用 __new__ 方法为对象分配内存空间

重写 __new__ 方法
重写的代码是固定的
重写 __new__ 方法一定要在最后 return super().__new__(cls) 
如果不 return（像上面代码栗子一样），Python 的解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法（__init__）
重点：__new__ 是一个静态方法，在调用时需要主动传递 cls 参数
'''
class test:
    def __new__(cls, *args, **kwargs):
        print("分配内存地址")
        instance = super().__new__(cls)
        print(id(instance))
        return instance
    def __init__(self):
        print("初始化对象")
        print(id(self))

t = test()

import sys
print(sys.path)
while True:
    print("test")