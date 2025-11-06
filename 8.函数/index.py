from typing import TypeVar 
# 下面这样导入，可以导入指定函数,as可以给函数重命名
from module import add as moduleAdd
# 下面这样可以把模块里面的方法全部导入，as是重命名
# 注意，这种写法导入的方法不能直接用，需要通过module2.methodName来调用，这里改了别名，所以是myModule2.methodName
import module2 as myModule2
# 如果要把所有函数全部导入到当前模块，并且希望可以直接使用，可以用下面的方式（并不推荐）
from module import *;# 这样就把所有的函数全部导入了，在这个文件里面可以直接使用module中的所有函数，不需要导入
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

# * 和大多数编程语言一样，默认值参数必须在没有默认值的参数之后，否则在静态检查时就会报错

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

# 注意，python中的泛型不能显式传递，完全依靠自动推断

# python中，参数传递不仅可以用位置参数，还可以用命名参数，命名参数在python中一般称为关键字参数

def methodDemo6(param1,param2):
    """methodDemo6
    命名参数的测试
    """
    print("methodDemo6",param1,param2);
# 调用函数，使用命名参数
methodDemo6(param2 = "b",param1 = "a");
# 调用函数，使用位置参数
methodDemo6("a","b");
# 可以同时传递
methodDemo6("a",param2 = "b"); # 报错，位置参数必须在命名参数之前
# 如果同时传递位置参数和命名参数，不能乱传
# methodDemo6(param1 = "b","b"); # 位置参数必须在命名参数之前，报错
# methodDemo6("a","b",param1 = "b"); # 给param1赋值了两次，报错

#python允许不定参，通过*来定义
def methodDemo7(*params):
    """methodDemo7
    不定参的测试
    """
    print("methodDemo7",params);
    print(type(params));# 这里是一个元组，也就是只读的

methodDemo7("a","b","c");# 传递多少个参数都会被接收

# 由于python支持命名参数，所以不定参不一定是最后一个参数，但如果不定参后面还有参数，就必须用命名参数来调用了
def methodDemo8(*params,param2):
    """methodDemo8
    不定参的测试
    """
    print("methodDemo8",params,param2);

methodDemo8("a","b","c",param2 = "d");# 不定参后面的参数只能用命名参数传递了

# 上面一个*的不定参可以收集任意个数的位置参数，如果我们要收集任意个数的命名参数，需要用**
def methodDemo9(**params):
    """methodDemo9
    不定参的测试
    """
    print("methodDemo9",params);
    print(type(params));# 这里是一个字典
methodDemo9(param1 = "a",param2 = "b");# 传递多少个参数都会被接收

# 模块测试
print(moduleAdd(1,2,3,4,5));
print(myModule2.moduleSum(1,2,3,4,5,6,7));

