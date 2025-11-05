# input函数可以让程序阻塞，等待用户输入一段文本
userInput = input("请输入一段文本：");# 参数为提示信息
print(userInput,type(userInput));

# input函数获取到的是一个字符串，如果需要获取数字等类型，需要进行类型转换
# 注意，如果用户输入的不是数字，会抛出错误，至于错误的处理，不是现在要讨论的范围
userInput = int(input("请输入一个数字："));
print(userInput,type(userInput));

# while循环也很简单，这个循环没有for循环那么常用
count = 0;
while count < 5:
    print(count);
    count += 1;

# 可以通过while循环，让用户选择退出
while True:
    userInput = input("请输入一段文本：");
    if userInput == "exit":
        break;
    print(userInput);

