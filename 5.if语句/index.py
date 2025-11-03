# python的if语句和常规语言不太该一样，没有括号
names = ["张三","李四","王五","赵六"];
for item in names:
    # if语句的核心逻辑区域，JS叫做布尔判定，python叫做条件测试，本质上也是一个表达式
    if item == "张三":# 注意这个和冒号
        # break，continue这些语句，python也是有的
        continue;
    print(item);

# 常见的条件运算符在python里面都有
print(1 == 1);# python中的布尔值都是大写字母开头
print(1 > 2);
print(1 != 2);
print(2 >= 2);

# 顺道一提python中的assert语法
assert(1 == 1,"ErrorMessage");#我喜欢这种
assert 1 == 1,"ErrorMessage";

# python的条件测试，逻辑运算通过and和or连接，而不是&&和||
print(True and False);
print(True or False);
# 当然也可以加括号增加可读性
print((True and False) or (True or False));

# python存在或、与短路
print(False and (1/0 == 0));# 与短路，不报错
print(True or (1/0 == 0));# 或短路，不报错
# python作为弱类型语言，和js一样，很容易发生类型转换，通常来说，空值会转为false，其他转为true
print(bool(""));# 空字符串转为false
print(bool(" "));# 空格转为true
print(bool(0));# 0转为false
print(bool(1));# 1转为true
print(bool([]));# 空列表转为false
print(bool([1,2,3]));# 非空列表转为true
print(bool(None));# None转为false

# 基于这种特性，可以用一些js常用的技巧
str = "";
str = str or "default";# 如果str转bool为False，就用default代替，常用来赋值
print(str);

arr = [];
arr and arr[0] = 1;# 如果arr布尔判定为true，就给arr[0]赋值为1，这个技巧常用于前置条件校验，防报错

