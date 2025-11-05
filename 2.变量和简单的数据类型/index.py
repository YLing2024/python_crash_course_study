# python中变量的使用极其简单，甚至连声明符号都不需要
message = "this is a message";
# 变量直接使用即可
print(message);
# 变量可以重新赋值
# python是没有内置常量的，这是值得注意的地方，python的常量都是以全大写的方式做编码层面的约定
message = "this is a new message";
# 下面这个代码没有句末分号，也是可以执行的，实际上句末分号是可选的
print(message)
# python中的字符串可以是单引号，也可以是双引号
message = 'this is a single quotation mark string';
print(message);
# python中的方法调用和其他语言类似
message = "this is a example";
print(message.title());# title方法用于以首字母大写的方式显示句子
# 类似的，还有upper和lower方法，这两种方法通常用于忽略大小写的匹配中
print(message.upper());# upper方法用于将字符串转换为大写
print(message.lower());# lower方法用于将字符串转换为小写

# python中也有插值表达式，在字符串前面加上f或者F(format)，后面的字符串就可以用插值语法了，python中的插值语法 大括号，没有美元符号
name = "james";
age = 20;
print(f"my name is {name}, and i am {age} years old");
print(F"my name is {name}, and i am {age} years old");# F也是可以的

# python中使用strip来清理左右空格，而非更常用的trim
stripTest = "  123   ";
print(stripTest.strip());# strip方法用于清理左右空格
print(stripTest.lstrip());# lstrip方法用于清理左空格
print(stripTest.rstrip());# rstrip方法用于清理右空格

# python有一个removeprefix方法用于移除字符串的前缀
prefixTest = "http://www.baidu.com";
prefixTest2 = "www.google.com";
removePrefix = "http://";
print(prefixTest.removeprefix(removePrefix));# 移除了前缀
print(prefixTest2.removeprefix(removePrefix));# 前缀不匹配，没有移除前缀
#有移除前缀，自然就有移除后缀
suffixText = "baidu.com";
suffixText2 = "google";
removeSuffix = ".com";
print(suffixText.removesuffix(removeSuffix));# 移除了后缀
print(suffixText2.removesuffix(removeSuffix));# 后缀不匹配，没有移除后缀

# python中自然也有数字类型，但是分整数和浮点数，他们是有清晰边界的，这一点和JS不一样
print(1.0); # 输出的是1.0，并不是1，因为这里1.0表示的是一个浮点数
num1 = 3;
num2 = 2;
# 常见运算符都有
print(f"{num1 } + {num2 } = {num1 + num2}");
print(f"{num1 } - {num2 } = {num1 - num2}");
print(f"{num1 } * {num2 } = {num1 * num2}");
print(f"{num1 } / {num2 } = {num1 / num2}");
print(f"{num1 } // {num2 } = {num1 // num2}");# 双斜杠表示整除，会去掉小数部分
print(f"{num1 } % {num2 } = {num1 % num2}");
print(f"{num1 } ** {num2 } = {num1 ** num2}");# 乘方运算符
# python会自动忽略数字中的下划线，下划线可以用来分割数字方便阅读
print(1_000_000);
# 小数也是可以的
print(1_000_000.01_1);
# python整数有可能向浮点数转换
print(2/1);# 两个整数相除，结果一定是浮点数，所以这里是2.0
print(2 + 0.1 + 0.9);# 不管什么数值运算，只要运算中出现了浮点数，最后的结果一定是浮点数

#python可以快速给多个变量赋值
var1,var2,var3 = 1,2,3; # 同时给三个变量赋值
print(var1);
print(var2);
print(var3);

# 变量是可以有类型标注的，下面是常见的内置类型，python的数据类型没有任何强制性，仅仅是文档层面的标注，python解释器不会检查变量的类型是否匹配
# 如果要做类型的静态检查，需要依赖类型检查工具，比如mypy
a: int = 10
b: int = -5
c: int = 0x10  # 十六进制（16）
d: int = 0o10  # 八进制（8）
e: int = 0b10  # 二进制（2）
f: float = 3.14
g: float = 1.2e5  # 科学计数法（120000.0）
h: float = -0.0001
i: complex = 3 + 4j
j: complex = 1.5j  # 纯虚数（实部为0）
k: bool = True
l: bool = False
m: None = None
n: str = "Hello"
o: str = 'Python'
p: str = """多行字符串"""
q: list = [1, "a", True, 3.14]
r: list = []  # 空列表
s: tuple = (1, 2, 3)
t: tuple = (4,)  # 单元素元组需加逗号
u: tuple = ()  # 空元组
v: set = {1, 2, 3}
w: set = set([1, 2, 2, 3])  # 去重后 {1,2,3}
x: set = set()  # 空集合（不能用 {}，{} 是字典）
y: frozenset = frozenset({1, 2, 3}) # 冻结集合，不可变
z: dict = {"name": "Alice", "age": 20}
aa: dict = {}  # 空字典
ab: dict = dict(name="Bob", age=25)  # 另一种创建方式
ac: bytes = b"hello"  # 前缀 b 表示字节串
ad: bytes = bytes([104, 101, 108, 108, 111])  # 对应 "hello"，字节串
ae: bytearray = bytearray(b"hello")# 直接数字
af: range = range(10)  # 0-9
ag: range = range(1, 10, 2)  # 1,3,5,7,9
ah: bytes = b"Python"
ai: memoryview = memoryview(ah)
print(ai[0])  # 输出 80（'P' 的 ASCII 码）