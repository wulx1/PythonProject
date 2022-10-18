#读取文件
def readline():
    result = []
    with open("/Users/wulongxing/Desktop/test/test.txt") as file:
        for i  in file:
            i = i[:-1]
            result.append(i.split(","))
        print(result)
        return result
#文件排序
def sort_data(data):
    return sorted(data, key=lambda x: int(x[2]), reverse=True)
#写入文件
def write_file(datas):
    with open("/Users/wulongxing/Desktop/test/outtest.txt","w+") as file:
        for i in datas:
            file.write(",".join(i)+"\n")


data = readline()
datas = sort_data(data)
print(datas)
write_file(datas)

