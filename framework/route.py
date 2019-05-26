#encoding=utf-8
# 定义路由列表
route_list = []

# 定义带有参数的装饰器——用于给控制器函数分配路由
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器装饰指定函数的时候，把路径和函数添加到路由列表
        route_list.append((path, func))

        def inner():
            # 执行指定函数
            return func()

        return inner
    # 返回装饰器
    return decorator

