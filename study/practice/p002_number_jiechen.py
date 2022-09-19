'''实现阶层的结果'''
number = int(input("请输入你要计算的阶层："))
result = 1
while number> 0 :
    result = result*number
    number = number -1
print(result)

