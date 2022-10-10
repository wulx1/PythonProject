#!/user/bin/python
# !coding=utf-8
# -*- coding: utf-8 -*-
# import sys
# import difflib
# import re
# import os
#
#
# # --------------------------------比对两文件，将结果存入Result.html-------------------------------------------#
#
# # 读取配置文件函数
# from past.builtins import raw_input
#
#
# def read_file(file_name):
#     try:
#         file_handle = open(file_name, 'r')
#         text = file_handle.read().splitlines()  # 读取后以行进行分割
#         file_handle.close()
#         return text
#     except IOError as error:
#         print(f'Read file Error: {0}'.format(error))
#         sys.exit()
#
#
# # 比较两个文件并输出html格式的结果
# def compare_file(file1_name, file2_name):
#     if file1_name == "" or file2_name == "":
#         print(f'文件路径不能为空：file1_name的路径为：{0}, file2_name的路径为：{1} .'.format(file1_name, file2_name))
#         sys.exit()
#     text1_lines = read_file(file1_name)
#     text2_lines = read_file(file2_name)
#     diff = difflib.HtmlDiff()  # 创建htmldiff 对象
#     result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
#     #  将结果保存到result.html文件中并打开
#     try:
#         with open('result.html', 'w') as result_file:  # 同 f = open('result.html', 'w') 打开或创建一个result.html文件
#             result_file.write(result)  # 同 f.write(result)
#     except IOError as error:
#         print(f'写入html文件错误：{0}'.format(error))
#
#
# # ------------------------------------取出不同部分存入Result.txt-------------------------------------------#
#
# # 取出不同部分存入Result.txt
# def result(file1_name, file2_name):
#     if file1_name == "" or file2_name == "":
#         print(f'文件路径不能为空：file1_name的路径为：{0}, file2_name的路径为：{1} .'.format(file1_name, file2_name))
#         sys.exit()
#     str1 = []
#     str2 = []
#     str_dump = []
#     # 将A.txt的内容逐行读到str1中
#     with open(file1_name, 'r') as fa:  # 相当于fa=open(file1_name,'r')
#         for line in fa.readlines():
#             str1.append(line.replace("\n", ''))  # line.replace("\n",'') 去掉换行符\n
#     # 将B.txt中的内容逐行读到str2中
#     with open(file2_name, 'r') as fb:
#         for line in fb.readlines():
#             str2.append(line.replace("\n", ''))
#
#     # 将两个文件中重复的行，添加到str_dump中
#     for i in str1:
#         if i in str2:
#             str_dump.append(i)
#
#     # 将两个文件的行合并，并去重
#     str_all = set(str1 + str2)
#
#     # 将重复的行，在去重的合并行中，remove掉，剩下的就是不重复的行了
#     for i in str_dump:
#         if i in str_all:
#             str_all.remove(i)
#     # 写入文件中
#     with open("Result.txt", 'w+') as fc:
#         for i in list(str_all):
#             fc.write(i + '\n')
#     fa.close()
#     fb.close()
#     fc.close()
#
#
# if __name__ == "__main__":
#     x = raw_input(u"请输入第一个文件路径：")
#     y = raw_input(u"请输入第二个文件路径：")
#     compare_file(x, y)  # 传入两文件的路径
#     result(x, y)  # 传入两文件的路径


# # difflib模块作为python的标准库模块，无需安装，作用是比对文本之间的差异，且支持输出可读性比较强的html格式。
#
#
# import sys
# import difflib
#
#
# # 读取配置文件函数
# def read_file(file_name):
#     try:
#         file_handle = open(file_name, 'r')
#         text = file_handle.read().splitlines()  # 读取后以行进行分割
#         file_handle.close()
#         return text
#     except IOError as error:
#         print(f'Read file Error: {0}'.format(error))
#         sys.exit()
#

# # 比较两个文件并输出html格式的结果
# def compare_file(file1_name, file2_name):
#     if file1_name == "" or file2_name == "":
#         print(f'文件路径不能为空：file1_name的路径为：{0}, file2_name的路径为：{1} .'.format(file1_name, file2_name))
#         sys.exit()
#     text1_lines = read_file(file1_name)
#     text2_lines = read_file(file2_name)
#     diff = difflib.HtmlDiff()  # 创建htmldiff 对象
#     result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
#     #  将结果保存到result.html文件中并打开
#     try:
#         with open('result.html', 'w') as result_file:  # 同 f = open('result.html', 'w') 打开或创建一个result.html文件
#             result_file.write(result)  # 同 f.write(result)
#     except IOError as error:
#         print(f'写入html文件错误：{0}'.format(error))
#
#
# if __name__ == "__main__":
#     compare_file(r'C:\Users\os_wulx\Desktop\test1\test.txt', r'C:\Users\os_wulx\Desktop\test2\test.txt')  # 传入两文件的路径
