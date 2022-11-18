# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
# 自定义异常 需要继承Exception

class MyException(Exception):

    def __init__(self, *args):
        self.args = args


# raise MyException('爆出异常吧哈哈')


class modifyJsonError(MyException):
    def __init__(self, code=100, message='修改json异常', args=('修改json异常',)):
        self.args = args
        self.message = message
        self.code = code


class loginoutError(MyException):
    def __init__(self):
        self.args = ('退出异常',)
        self.message = '退出异常'
        self.code = 200


# raise loginError() # 这里突然返现 raise引发的异常将中断程序
#
try:
    raise loginoutError()
except loginoutError as e:
    print(e)  # 输出异常
    print(e.code)  # 输出错误代码
    print(e.message)  # 输出错误信息