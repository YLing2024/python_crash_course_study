# 字典(dict)是python对HashMap的一种实现
# 写法和JS对象类似
key = "isGirl"
testDict = {
    "name":"张三",
    "age":18,
    key:False,# 可自动识别key，在js中需要加括号
};
print(testDict);
# 通过中括号访问字典值，注意，这个key如果不存在，直接报错，不会返回None
print(testDict["name"]);
print(testDict[key]);
# 提供的方法是get，这个方法是安全的，如果不存在返回None，不会报错
print(testDict.get("weight"));
print(testDict.get("weight" ,180));# 可以指定默认值，若不存在则返回默认值

# 添加值的方式和其他语言也是很类似的
testDict["height"] = 180;
print(testDict);
# 提供的api为update，传入一个新的字典，其实效果类似于assign
testDict.update({
    "age":19,
    "height":181,
});
print(testDict);

# 通过pop方法可以删除某个元素
testDict.pop("height");
print(testDict);
# 通过popItem可以删除最后一个插入的元素
testDict.popitem();
print(testDict);
#还记得list那里的del吗？del也可以用来删除dict中的元素
del testDict["age"];
print(testDict);

# 为了遍历字典，我们先引出几个方法
testDict["weight"] = 70;
keys = testDict.keys();
print(keys);
values = testDict.values();
print(values);
items = testDict.items();
print(items);
# 上面三个东西返回的是试图对象，类似于数据库里面的视图，或者说是getter，实时同步，不占多余内存
# ! 这里书里提到keys和values是list，应该是错的，要注意
# 这仨也是可迭代的
for key in keys:
    print(key);
for value in values:
    print(value);
for item in items:
    print(item);
    print(type(item)); # 这玩意儿是一个tuple
    print(item[0],item[1]); # 可以直接通过访问tuple的语法访问
# 如果直接遍历字典，获取的是key，和遍历keys完全等价
for key in testDict:
    print(key);
# items很特殊，可以拿两个变量来接受，就可以得到两个值
for key,value in items:
    print(key,value);
# 上面的写法本质上是自动解包的语法糖，自动解包类似于js的解构赋值
for item in items:
    key,value = item;# 可以直接手动解包
    print(key,value);
    print(item[0],item[1]);# 由于是元组，也可以按照元组的方式访问

# python提供了集合类型
setTest = set([1,2,3,4,5,6,1,2,3,4,5]);
print(setTest); # 自动去重
setTest2 = {1,2,3,4,5,6,7,8,9,10,1};# 集合可以直接写字面量
print(setTest2);

