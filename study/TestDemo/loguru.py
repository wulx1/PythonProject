#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


def decorator(fun):
    def fun1():
        print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        fun()
    return fun1

@decorator
def aaa():
    print("转装饰器用法")
aaa()
user = 'wulx'
print(len(user))
print(user.count('w'))




