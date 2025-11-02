# python中的数组叫做列表，字面量和大多数编程语言一样，用方括号表示
listTest = ["a","b","c"];
print(listTest);
# 访问列表元素的方法也和大多数语言一致，用方括号
print(listTest[0]);
# python的下标支持负数，-1代表最后一个元素，-2代表倒数第二个元素，以此类推
print(listTest[-1]);
#> 实际上JS原生也提供了这种方式，只不过是用at方法提供的，不支持这种字面量直接写
# 修改元素也没什么特别的
listTest[2] = "d";
print(listTest);
# 使用append方法可以在末尾添加元素
listTest.append("e");
print(listTest);
# insert可以在指定位置插入元素
listTest.insert(1,"f");
print(listTest);
# pop方法可以删除掉指定位置的元素
listTest.pop(2);
print(listTest);
listTest.pop(); # 如果不传参数，默认删除最后一个元素
print(listTest);
# remove方法可以删除掉指定元素
listTest.remove("a");
print(listTest);
# 只会删除匹配到的第一个元素
listTest.append("a");
listTest.append("a");
listTest.remove("a");
print(listTest);
# 还可以通过del关键字删除指定位置的元素
del listTest[0];
print(listTest);

# python内置了很多列表排序方法
listTest2 = ["e","c","a","d","b"];
print(listTest2);
# sort方法可以对列表进行排序，默认是升序，改变的是列表本身，这个函数并不是纯函数
listTest2.sort();
print(listTest2);
# 也可以传入参数，指定降序
listTest2.sort(reverse=True);
print(listTest2);
# sort函数也支持回调自定义排序，通过key参数传入，涉及到匿名函数，后面再说
# sorted函数是sort函数的纯函数版本，返回一个排序后的拷贝
listTest2_sorted = sorted(listTest2);
print(listTest2_sorted);
print(listTest2);# 原列表不会被改变
# python提供了reverse方法用于列表的反转
listTest2.reverse();
print(listTest2);
# 同样也有纯函数版本，注意，这里返回的是一个迭代器
listTest2_reversed = reversed(listTest2);
print(listTest2_reversed);
print(list(listTest2_reversed));# 可以通过list函数将迭代器转为列表
print(listTest2);# 原列表不会被改变
#! 需要格外注意，reversed和sorted这种纯函数版本，都是通过全局函数提供的

# 一个小思考，为什么python中的sorted和reversed这种方法是全局方法
# 实际上，sorted方法和reversed方法都是将可迭代对象转为list后统一处理的，例如sort方法，类似于先迭代生成一个拷贝，然后调用拷贝的sort方法
# 为什么不直接在list抽象层提供呢？因为可迭代对象都可以转为list，但是可迭代对象并不一定有sort方法，例如元组，元组是不可变的，不能排序，但是可以通过sorted返回一个排序后的列表，所以sorted方法应该和sort解耦

# 可以通过len函数获取列表长度
print(len([1,2,3]));