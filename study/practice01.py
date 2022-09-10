'''
做一个通讯录系统
功能模块有以下几点
1、增加联系人
2、列出联系人
3、查询联系人
4、删除联系人
5、修改联系人

'''
persons =[]

def add_oerson():
    name = input("请输入想要添加的姓名:")
    address = input("请输入想要添加的地址:")
    phone = input("请输入想要添加的号码:")
    if name and address and phone:
        person = {
            "name":name,
            "address":address,
            "phone":phone
        }
        persons.append(person)
        print("添加成功！")

def list_person():
    print("当前通讯录的联系人为：" )
    for person in persons:
        print(person)

def select_person():
    str_name = input("请输入你想要查询的姓名：")
    for person in persons:
        if str_name == person["name"]:
            print("当前联系人信息如下：")
            print(person)
        elif str_name != person["name"]:
            print("查无此人")

def delete_person():
    str_name = input("请输入你想删除的联系人姓名：")
    for person in persons:
        if str_name == person["name"]:
            persons.remove(person)
            print("删除成功，当前联系人有:" )
            print(persons)


def update_person():
    update_name = input("请输入你要修改人的姓名")
    for person in persons:
        if update_name == person["name"]:
            update_name =input("请输入修改后的姓名：")
            update_address = input("请输入修改后的地址：")
            update_phone = input("请输入修改后的电话：")
            person1 = {
                "name": update_name,
                "address": update_address,
                "phone": update_phone
            }
            print("修改后的联系人信息如下：")
            print(person1)
            persons.append(person1)
        else:

            print("无此联系人")
def main1():
    print("---欢迎来到通讯录查询系统---")
    print("---请输入你想要的功能---")
    while True:
        print("---你可以继续选择功能---")
        print("1、增加联系人")
        print("2、列出联系人")
        print("3、查询联系人")
        print("4、删除联系人")
        print("5、修改联系人")
        print("6、退出程序！")


        str = input("请输入你想要的功能:  ")
        if str == '1':
            add_oerson()
        elif str == '2':
            list_person()
        elif str == '3':
            select_person()
        elif str == '4':
            delete_person()
        elif str == '5':
            update_person()
        elif str == 6:
            quit()
        else:
            print("你的输入无效")

























# persons=[]
#
# #添加联系人
# def create_person():
#     name = input("请输入姓名")
#     address = input("请输入地址")
#     phone =input("请输入手机号码")
#
#     if name and address and phone:
#         person = {
#             "name":name,
#             "address":address,
#             "phone":phone
#         }
#         persons.append(person)
#         print("添加成功！")
#
#
# #列出联系人
# def list_persoon():
#     for person in persons:
#         print(person)
#
#
# #查询联系人
# def select_person():
#     name = input("请输入你想查找的姓名：")
#     for person in persons:
#         if name == person["name"]:
#             print(person)
#
# #删除联系人
# def delete_person():
#     name = input("请输入你想删除的联系人姓名：")
#     for person in persons:
#         if name == person["name"]:
#             persons.remove(person)
#
# def main():
#     while True:
#         print("wecome to persons manage,you can use many able")
#         input_str = input("1.create person\n"
#                           "2.list person\n"
#                           "3.select person\n"
#                           "4.delete person\n"
#                           "5.quit\n")
#         if input_str == "1":
#             create_person()
#         elif input_str == "2":
#             list_persoon()
#         elif input_str == "3":
#             select_person()
#         elif input_str == "4":
#             delete_person()
#         elif input_str =="5":
#             quit()
#         else:
#             print("您的输入无效！")

if __name__ == '__main__':
    main1()



