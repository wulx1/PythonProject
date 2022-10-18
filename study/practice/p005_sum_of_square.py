'''求前N个数字平方和'''
number = int(input("请输入你要计算的平方和数字："))
result = 0
for i in range(1,number+1):
    result = result + i*i
print(result)