'''有一个数据list of dict如下

a = [

    {"test1": "123456"},

    {"test2": "123456"},

    {"test3": "123456"},

]

写入到本地一个txt文件，内容格式如下：

test1,123456

test2,123456

test3,123456'''

lists = [
    {"test1":"123456"},
    {"test2":"123456"},
    {"test3":"123456"}
]
with open("/Users/wulongxing/Desktop/test/test.txt","w+",encoding="utf-8") as f:
    for data in lists:
        print(data,',',end="")
        for key,value in data.items():
            f.write(f"{key},{value}\n")

