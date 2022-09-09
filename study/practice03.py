'''
PyMySQL
pip install pymysql
'''
import pymysql
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1234567890',
    db='MockServer',
    charset='utf8'
)
cursor= db.cursor()
cursor.execute("select * from api")
data = cursor.fetchone()
print(data)
cursor.close()

pymysql.connect(
    host="locahost",
    port=3306,
    user='root',
    password='123456',
    db='test',
    charset='utf-8'
)