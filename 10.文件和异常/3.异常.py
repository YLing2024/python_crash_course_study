import traceback  # 导入 traceback 模块
# python中的异常处理，用的是try-except，而不是try-catch，注意

#依旧沿用python的语言风格
try:
    print(1/0);
except:# 会捕获代码块所有错误
    print("出现了错误");
finally:# 也有finally
    print("finally");

try:
    print(1/0);
except ZeroDivisionError:# 可以指定捕获的错误类型
    print("出现了除0错误");

try:
    code = 1 / 2;
except ZeroDivisionError:
    print("出现了除0错误");
else: # python新搞出来一个else，这个else会在没有异常的情况下运行，并且else会获取到try代码中的上下文
    print(code);
finally: # 也有finally，finally会在else之后运行
    print("finally");

try:
    code = 1 / 2;
except ZeroDivisionError:
    # 这里面至少有一个语句，如果确实什么都不做，需要用pass语句,python没有空语句
    pass;

try:
    code = 1/0;
except ZeroDivisionError as error: # 这样获取错误对象，注意，一个except只能捕获一种错误，如果要捕获多种错误，需要多个except语句
    print("出现了除0错误");
    print(error); # 可以打印错误对象
    traceback.print_exc(); # 可以打印错误对象的栈轨迹，查看错误发生的位置
print("程序继续运行");

# 可以使用raise手动抛出异常
try:
    print(1/0);
    raise;# 如果不写具体的错误，在正常代码块中，没有任何问题
except ZeroDivisionError:
    print("出现了除0错误");
    raise; # 如果不写具体的错误，在异常代码块中，相当于rethrow

# 下面的代码不会执行
raise ZeroDivisionError("手动抛出除0错误");