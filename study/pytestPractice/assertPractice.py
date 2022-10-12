'''
前言
与unittest不同，pytest使用的是python自带的assert关键字来进行断言
assert关键字后面可以接一个表达式，只要表达式的最终结果为True，那么断言通过，用例执行成功，否则用例执行失败
'''
def fun():
    return 3
def test_fun():
    a = fun()
    assert a % 2 ==0,'判断a为偶数，当前a的值为:%s' %a