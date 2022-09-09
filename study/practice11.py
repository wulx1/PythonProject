'''
try语句的工作原理
首先，执行  try 子句

如果没有异常发生，则不执行  except 里面的代码，并执行  try 里面剩下的代码。

如果在执行 try 里面代码时发生了异常，则不再执行剩下代码，如果抛出异常的类型和  except 的异常类匹配，则执行  except 里面的代码

如果抛出的异常没有被 except 的异常类匹配上，则直接抛出原生异常，在控制台打印


'''

import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
# else:
#     print("没异常才执行")

def test():
    while True:
        try:
            print("没异常的print")
            return "try"
        except ValueError:
            print("d ")
        else:
            print("没异常才执行")
            return "else"
print(test())

