'''
前言
目前有两种纯测试的测试框架，pytest和unittest
unittest应该是广为人知，而且也是老框架了，很多人都用来做自动化，无论是UI还是接口
pytest是基于unittest开发的另一款更高级更好用的单元测试框架
出去面试也好，跟别人说起来也好，pytest的逼格明显高于unittest


为什么要用Pytest
pytest 的官方网站介绍，它具有如下特点：
非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
能够支持简单的单元测试和复杂的功能测试
支持参数化
执行测试过程中可以将某些测试跳过（skip），或者对某些预期失败的case标记成失败
支持重复执行(rerun)失败的 case
支持运行由 nose, unittest 编写的测试 case
可生成 html 报告
方便的和持续集成工具 jenkins 集成
可支持执行部分用例
具有很多第三方插件，并且可以自定义扩展
'''

def func(x):
    return  x+1
def test_answer():
    assert func(3) == 5

class Testcase:
    def test_01(self):
        x = 'this'
        assert 'h' in x
    def test_02(self):
        x = 'hello'
        assert hasattr(x,'check')

'''
知识点
@pytest.mark.skip 可以加在函数上，类上，类方法上
如果加在类上面，类里面的所有测试用例都不会执行
以上小案例都是针对：整个测试用例方法跳过执行，如果想在测试用例执行期间跳过不继续往下执行呢？

pytest.skip()函数基础使用
'''