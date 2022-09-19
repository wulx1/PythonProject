'''判断一个区间的素数'''
for i in range(10, 25):
    list01 = []
    for j in range(2, i):
        list01.append(str(i % j))
    if "0" not in list01:
        print(i)

x= int(input("请输入你要判断的数:"))
for i in range(2,x):
    if x % i ==0:
        print(f'{x}不是素数')
    else:
        print(f"{x}是素数")