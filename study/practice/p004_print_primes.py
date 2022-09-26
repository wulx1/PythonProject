'''判断一个区间的素数'''
from math import sqrt

# for i in range(10, 25):
#     list01 = []
#     for j in range(2, i):
#         list01.append(str(i % j))
#     if "0" not in list01:
#         print(i)

# x= int(input("请输入你要判断的数:"))
# for i in range(2,x):
#     if x % i ==0:
#         print(f'{x}不是素数')
#     else:
#         print(f"{x}是素数")
#

def is_primes(number):
    if number in range(1,2):
        return True
    for i in range(2,number):
        if number%i == 0:
            return False
    return True


def print_primes(beagin,end):
    for number in range(beagin,end+1):
        if is_primes(number):
            print(f'{number} is primes')
        else:
            print(f'{number} is not primes')

bedin = 11
end = 25
print_primes(bedin,end)