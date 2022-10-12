'''
用过unittest的童鞋都知道，有两个前置方法，两个后置方法；分别是

setup()
setupClass()
teardown()
teardownClass()
Pytest也贴心的提供了类似setup、teardown的方法，并且还超过四个，一共有十种

模块级别：setup_module、teardown_module
函数级别：setup_function、teardown_function，不在类中的方法
类级别：setup_class、teardown_class
方法级别：setup_method、teardown_method
方法细化级别：setup、teardown
'''