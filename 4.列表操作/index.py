from collections.abc import Iterable # 这个abc是abstract base class
# 我们可以使用for in循环遍历数组
forInTest = [1,2,3,4];
for item in forInTest: # 注意语法细节，后面有个冒号，python不依靠大括号来判断代码块，而是依靠缩进
    print(item);# 这里的for in循环得到的直接是item，类似于js中的for of循环
print(item); # 循环结束后，迭代变量依然存在，指向最后一个元素
# python中的列表可以存储任意数据类型，和JS类似
forInTest = [1,"1",1.0];
for item in forInTest:
    print(item);

# range函数可以用于快速生成可迭代对象，这是函数一般用来配合for循环使用
print(range(1,5));
print(isinstance(range(1,5), Iterable));# 这里可以验证（需要导入Iterable类型）
# 既然range生成的是可迭代对象，自然可以被for循环遍历，下面就很类似其他语言中普通的for循环了
forInTest = ["a","b","c","d"];
for i in range(0,len(forInTest)): # 需要注意，range函数生成的是序列是包前不包后的，很多计算类函数都是这样，不仅限于python，即range(a,b)生成的序列为a到b-1，不包含b。
    print(i);
    print(forInTest[i]);
# range还支持单个参数，单个参数的时候，range从0开始
for i in range(4):
    print(i);
# 前面提过，list可以传入一个可迭代对象来初始化，当然也可以传入range
print(list(range(1,4)));
# range是可以指定步长的，第三个参数，默认步长为1
print(list(range(1,11,2))); # 这里打印的就是1-10的奇数

# 下面是一个计算斐波那契数列(count > 2)的小例子
count = 10;
list = [];
prevPrev = 1;
prev = 1;
list.append(prevPrev);
list.append(prev);
for i in range(2,count + 1):
    list.append(prevPrev + prev);
    prevPrev = prev;
    prev = list[i];
print(list);

# python有一些常用的用于数值统计的方法，虽然自己实现也很简单，但是既然有现成的，不用白不用
print(min([1,2,3,4,5])); # 这里打印的就是1-5中的最小值1
print(max([1,2,3,4,5])); # 这里打印的就是1-5中的最大值5
print(sum([1,2,3,4,5])); # 这里打印的就是1-5的和15
# 很显然，这几个方法既然作为全局函数提供，自然是可以作用于任何可迭代对象的，用range为例
print(min(range(1,6))); # 这里打印的就是1-5中的最小值1
print(max(range(1,6))); # 这里打印的就是1-5中的最大值5
print(sum(range(1,6))); # 这里打印的就是1-5的和15

# 下面这种语法是列表推导，是一种很新的语法，可以多练几遍
squares = [value**2 for value in range(1,11)];
print(squares);

# 要截取子列表，可以使用切片语法，这和JS很不一样，切片语法并不是通过slice方法提供的，而是一种专门的语法
print([1,2,3,4,5][1:3]); # 截取下标为1-3的，包前不包后，所以结果是[2,3]
# 切片语法适用于所有有序类型(sequence types),包括list，str，tuple等
print("1234567"[1:5]); # 截取下标1-5，包前不包后，所以是"2345"
# 切片语法的两个数都可以省略，甚至可以同时省略
print([1,2,3,4,5][1:]); # 省略第二个数，从下标1开始截取到最后
print([1,2,3,4,5][:3]); #省略第一个数，从最开始截取到下标为3的数，不包含下标3
print([1,2,3,4,5][:]);# 全部省略，截取整个列表

# 和JS的slice一样，切片语法可以很容易得完成数组的浅拷贝
list1 = [1,2,3,4,5];
# 直接赋值
list2 = list1;
list1[0] = 0;
# list1和list2同步改变
print(list1);
print(list2);
# 切片赋值
list2 = list1[:];
list1[0] = 1;
#list2 不随着list1去改变
print(list1);
print(list2);

# 切片语法允许传入负数下标
print([1,2,3,4,5][-3:-1]); # 从倒数第三个开始截取到倒数第一个，不包含倒数第一个，所以结果是[3,4]

# 切片常见的应用就是切片遍历
list = ["a","b","c","d","e"];
for item in list[1:3]:
    print(item);
# 等价于下面的写法
for index in range(1,3):
    print(list[index]);

list1 = [1,2,3,4,5];
list2 = [1,2,3,4,5];
# 需要注意，python中 == 运算符比较的是值是否相等，而不是引用是否相等，这和绝大多数编程语言都是不一样的
print(list1 == list2);

# 元组(tuple)就是不可变的列表，下面就是一个元组
tuple = (1,2,3);
# tuple本身没有提供任何写入数据的方法，我们尝试直接修改会报错，如下：
# tuple[0] = 2;
print(tuple);
print(tuple[0]);
# tuple显然是可迭代的
for i in tuple:
    print(i);
# tuple也可以切片，切片后得到的也是tuple
tuple2 = tuple[:];
print(tuple2);
# 看个很高级的东西，元组是逗号做标识，可以没有小括号(元组只是值不可变，并不是变量本身不可变，python没有常量)
tuple = 1,2,3,4;
print(tuple);
# 因为元素是用逗号识别的，如果要定义只有一个元素的元组，必须在元素后面加一个逗号
tuple = 1,;
tuple2 = (2,);
print(tuple);
print(tuple2);

