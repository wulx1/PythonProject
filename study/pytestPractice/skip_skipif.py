'''
pytest.mark.skip  可以标记无法在某些平台上运行的测试功能，或者您希望失败的测试功能
希望满足某些条件才执行某些测试用例，否则pytest会跳过运行该测试用例
实际常见场景：跳过非Windows平台上的仅Windows测试，或者跳过依赖于当前不可用的外部资源（例如数据库）的测试

@pytest.mark.skip
跳过执行测试用例，有可选参数reason：跳过的原因，会在执行结果中打印
'''

import pytest
@pytest.fixture(autouse=True)
def login():
    print("---登陆---")

def test_01():
    print("这是测试用例1 ")

@pytest.mark.skip(reason = '该用例未写好，先不执行！')
def test_02():
    print("我是测试用例2")



