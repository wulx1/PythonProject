'''
python 对文件进行批量改名用到的是 os 模块中的 listdir 方法和 rename 方法。
os.listdir(dir)：获取指定目录下的所有子目录和文件名
os.rename(原文件名，新文件名）：对文件或目录改名

把混乱的文件名改成有序的文件名:
'''
import os
path = input("请输入你的路径")
filelist = os.listdir(path)
n = 0
for i in filelist:
    oldname = path +os.sep+ filelist[n]
    newname = path + os.sep + "test" + str(n) + '.txt'
    os.rename(oldname,newname)
    print(oldname,'---------',newname)
    n += 1
