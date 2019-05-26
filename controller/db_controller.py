import sys
import json
import route

sys.path.append("../model")
import my_cnf

# 获取首页数据
@route.route("/dbinfo.html")
def dbinfo():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0")]

    # 打开模板文件，读取数据
    with open("../template/index.html", "r") as file:
        file_data = file.read()

    # 查询sql语句
    sql = "select version();"
    # 执行sql
    my_cnf.cur.execute(sql)
    # 获取结果集
    result = my_cnf.cur.fetchone()
    # print(result)

    # 可拼接富文本html
    data = '''
    <s>%s</s>
    ''' % result

    # 替换模板文件中的模板遍历
    result = file_data.replace("{%content%}", data)

    return status, response_header, result

    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0")]

    # 打开模板文件，读取数据
    with open("../template/index.html", "r") as file:
        file_data = file.read()

    # 处理后的数据, 从数据库查询
    data = time.ctime()
    # 替换模板文件中的模板遍历
    result = file_data.replace("{%content%}", data)

    return status, response_header, result

# 个人中心数据接口开发
@route.route("/api/center_data.html")
def center_data():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0"), ("Content-Type", "text/html;charset=utf-8")]

    # 查询sql语句
    sql = "select host, user, authentication_string, plugin from user;"
    # 执行sql
    my_cnf.cur.execute(sql)
    # 获取结果集
    result = my_cnf.cur.fetchall()

    # 个人中心数据列表
    center_data_list = list()
    # 遍历每一行数据转成字典
    for row in result:
        # 创建空的字典
        center_dict = dict()
        center_dict["host"] = row[0]
        center_dict["user"] = row[1]
        center_dict["passwd"] = row[2]
        center_dict["plugin"] = row[3]
        # 添加每个字典信息
        center_data_list.append(center_dict)

    # 把列表字典转成json字符串, 并在控制台显示
    json_str = json.dumps(center_data_list,ensure_ascii=False)
    # print(json_str)
    return status, response_header, json_str

# 获取个人中心数据
@route.route("/center.html")
def center():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "PWS2.0")]

    # 打开模板文件，读取数据
    with open("../template/center.html", "r") as file:
        file_data = file.read()

    # 处理后的数据, 从数据库查询
    data = "ajax get data:"
    # 替换模板文件中的模板遍历
    result = file_data.replace("{%content%}", data)

    return status, response_header, result
