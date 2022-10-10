'''
test suite
测试套件，理解成测试用例集
一系列的测试用例，或测试套件，理解成测试用例的集合和测试套件的集合
当运行测试套件时，则运行里面添加的所有测试用例

test runner
测试运行器
用于执行和输出结果的组件
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
