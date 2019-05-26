"""miniweb框架，负责处理动态资源请求"""
import sys
import route

# 控制器函数文件——开始
sys.path.append("..\controller")
import index_controller
import db_controller

# 控制器函数文件——结束



# 没有找到动态资源
def not_found():
    # 响应状态
    status = "404 Not Found";
    # 响应头
    response_header = [("Server", "PWS2.0")]
    # 处理后的数据
    data = "route not found!"

    return status, response_header, data

# 处理动态资源请求——通过路由查找对应函数
def handle_request(env):
    # 获取动态请求资源路径
    request_path = env["request_path"]
    print("Framework Get Request:", request_path)
    # 遍历路由列表，选择执行的函数
    for path, func in route.route_list:
        if request_path == path:
            result = func()
            return result
    else:
        # 没有找到动态资源
        result = not_found()
        return result