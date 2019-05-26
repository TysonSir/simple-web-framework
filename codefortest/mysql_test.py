import pymysql

# 处理后的数据, 从数据库查询
conn = pymysql.connect(host="192.168.1.11",
                        port=3306,
                        user="root",
                        password="111111",
                        database="mysql",
                        charset="utf8")

# 获取游标
cursor = conn.cursor()
# 查询sql语句
sql = "select host, user, authentication_string, plugin from user;"
# 执行sql
cursor.execute(sql)
# 获取结果集
result = cursor.fetchall()
print(result)