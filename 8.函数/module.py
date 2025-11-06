# 一个文件就是一个模块

def add(*args):
    """add
    加法函数
    """
    result = 0;
    for arg in args:
        result += arg;
    # 可以直接 return sum(args)
    return result;