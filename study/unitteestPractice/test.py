'''
unittest简单介绍
单元测试框架
还可以适用WEB自动化测试用例的开发与执行
提供丰富的断言方法
官方文档：https://docs.python.org/zh-cn/3/library/unittest.html

测试用例
必须以“test_”开头命名的方法，否则无法识别并执行
方法里面需要有断言，才能在最后运行时有该用例的执行结果
可包含多个测试用例

'''
import unittest

class testCase(unittest.TestCase): #unittest.Testcase 自己创建的单元测试类都要继承它，它是所有单元测试类的基类

    def setUp(self) -> None:  #setUp 用于每个测试用例执行前的初始化工作，所有类中方法的入参为 self ，定义实例变量也要 self.变量

        print("case执行前")
    def tearDown(self) -> None: #tearDown 每个测试用例执行后的都会执行此方法
        print("case执行后")

    @classmethod #每个单元测试类运行前调用该方法，只会执行一次属于类方法，需要加上装饰器 @classmethod 默认入参是 cls ，指的就是“类对象”本身，其实和self没什么区别，用法一致

    def setUpClass(cls) -> None:
        print("对象执行前")

    @classmethod  #tearDownClass 每个单元测试类运行后调用该方法，只会执行一次属于类方法，需要加上装饰器 @classmethod
    def tearDownClass(cls) -> None:
        print("对象执行后")
    @unittest.skip("跳过")
    def test01(self):
        print("这是用例1")

    def test02(self):
        print("这是用例2")

    def test03(self):
        flag = False
        self.assertFalse(flag,msg="断言通过")

if __name__ == '__main__':
    unittest.main()

