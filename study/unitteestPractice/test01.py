'''
test suite
测试套件，理解成测试用例集
一系列的测试用例，或测试套件，理解成测试用例的集合和测试套件的集合
当运行测试套件时，则运行里面添加的所有测试用例

test runner
测试运行器
用于执行和输出结果的组件

包含知识点
使用测试套件时，测试用例的执行顺序可以自定义，按照添加的顺序执行
有两种添加测试用例的方式，推荐方式二，代码更少更快捷
addTests(tests) ，传入的 tests 可以是list、tuple、set
添加的测试用例格式是：单元测试类名(测试用例名)
使用测试套件执行测试用例的大致步骤是：实例化TestSuite - 添加测试用例 - 实例化TextTestRunner - 运行测试套件
测试套件也可以添加测试套件
'''
import unittest
class testCase(unittest.TestCase):
    def test_01(self):
        print("test01")

    def test_02(self):
        print("test02")

    def test_03(self):
        print("test03")

    def test_04(self):
        print("test04")

    def test_05(self):
        print("test05")

if __name__ == '__main__':

    #实例化测试套件
    suite = unittest.TestSuite()
    #实例化第二个测试套件
    suite1 = unittest.TestSuite()
    #添加测试用例--方式一
    suite.addTest(testCase('test_03'))
    suite.addTest(testCase('test_01'))
    suite1.addTest(testCase('test_03'))
    suite.addTest(testCase('test_01'))
    #添加测试用例--方式二
    testcase = (testCase('test_05'),testCase('test_04'))
    suite.addTests(testcase)
    #测试套件添加测试套件
    suite.addTest(suite1)
    runner = unittest.TextTestRunner()
    runner.run(suite)
