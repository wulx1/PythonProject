'''
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。
要求：
1. 校验输入内容是否符合规范（xx@polo.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾
2. 可以循环“输入--输出判断结果”这整个过程
3. 按字母 Q（不区分大小写）退出循环，结束程序
'''
import re

while True:
    email = input("请输入你的邮箱：")
    if email.upper()== "Q":
        break
    res =re.findall(".com$",email)
    if not res:
        print("error")
    temp = email.split("@")
    name = temp[0]
    com = temp[1].split(".")[0]
    print(f'usname:{name},companyname:{com}')



