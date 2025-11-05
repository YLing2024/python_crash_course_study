from typing import TypeVar 
# 函数定义使用def关键字

def sayHello():# 注意这里冒号
    print("Hello World!");
# 调用函数
sayHello();

# 函数注释一般用三引号，注意，三引号的注释一般在函数定义的下一行
def methodDemo():
    """methodDemo
    函数的注释一般是这么写的
    """
    print("methodDemo");

# 函数参数定义，传递，以及函数的返回值也非常简单
def methodDemo2(param1,param2):
    """methodDemo2
    函数参数定义和传递，返回值的测试
    """
    print("methodDemo2",param1,param2);
    # 函数可以有返回值
    return param1 + param2;
# 调用函数
result = methodDemo2("a","b");
print(result);
# 定义好的参数一般要传完，否则会报错
# result = methodDemo2("a");
# 也可以给参数默认值，给了默认值的参数可以不传
def methodDemo3(param1,param2 = "default"):
    """methodDemo3
    给参数param2设置默认值
    """
    print("methodDemo3",param1,param2);
# 调用函数，param2不传值，会使用默认值
methodDemo3("a");

# 函数的类型标注
def toInt(param:str) -> int:
    """toInt
    将字符串转换为整数
    """
    return int(param);
# 调用函数
result = toInt("123");
print(result);
print(type(result));
# python的类型标注只是一个文档，哪怕不是字符串，也可以传进去，不会报错
result = toInt(123);
print(result);
print(type(result));

# python的泛型标注相对麻烦

T = TypeVar("T"); # 定义一个泛型参数，TypeVar的参数用于调试，这个TypeVar在typing模块中
def methodDemo4(param:T) -> T:
    """methodDemo4
    泛型函数的测试
    """
    return param;
# 调用函数
result = methodDemo4("a"); # IDE会自动推断类型
print(result);

# python3.12支持更简单的泛型标注，不需要再定义TypeVar
def methodDemo5[S](param:S) -> S:
    """methodDemo5
    泛型函数的测试
    """
    return param;
result = methodDemo5("a");
print(result);

# 注意，python中的泛型不能显示传递，完全依靠自动推断