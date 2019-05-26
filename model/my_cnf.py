import pymysql

class my_cnf:
    
    config = {}
    conn = None
    cursor = None

    def __init__(self):
        # 处理后的数据, 从数据库查询
        self.config = {
            "host":"192.168.1.11",
            "port":3306,
            "user":"root",
            "password":"111111",
            "database":"mysql"
        }

        # 处理后的数据, 从数据库查询
        self.conn = pymysql.connect(host=self.config["host"],
                                port=self.config["port"],
                                user=self.config["user"],
                                passwd=self.config["password"],
                                db=self.config["database"],
                                charset="utf8")

        # 获取游标
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()

    def get_cursor(self):
        return self.cursor

# 定义数据库对象
my_cnf_obj = my_cnf()
# 定义游标
cur = my_cnf_obj.get_cursor()