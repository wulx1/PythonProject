'''
IO操作，读和写
'''
# f = open("/Users/wulongxing/Desktop/test.txt",mode='r')
# print(f)
# print(f.read())
# f.close()
# try:
#     f1 = open("/Users/wulongxing/Desktop/test.txt",mode='r')
#     print(f1.read())
# finally:
#     if f1:
#          f1.close()
#
# with open("/Users/wulongxing/Desktop/test.txt") as f2:
#     print(f2.read())
import os

# file = open("/Users/wulongxing/Desktop/test.txt",mode='w+')
# file.write("大帅哥")
# file.writelines("wulongxing,hello world!")
# print(file.read())
#
# # with open("/Users/wulongxing/Desktop/test.txt",mode='r') as f:
# #     print(f.read())
#
# path = os.getcwd()
# for dirpath, dirnames, filenames in os.walk(path):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#
import os

path = input('请输入文件路径(结尾加上/)：')

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

n = 0
for i in fileList:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = path + os.sep + 'a' + str(n + 1) + '.JPG'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    n += 1


