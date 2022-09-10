# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from study.practice01 import create_person,list_persoon,delete_person,select_person


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        input_str = input("1.create person\n"
                          "2.list person\n"
                          "3.select person\n"
                          "4.delete person\n"
                          "5.quit\n")
        if input_str == "1":
            create_person()
        elif input_str == "2":
            list_persoon()
        elif input_str == "3":
            select_person()
        elif input_str == "4":
            delete_person()
        elif input_str == "5":
            quit()
        else:
            print("您的输入无效！")
            print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
