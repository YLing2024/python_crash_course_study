# 类一般大驼峰
class Dog:
    
    """Dog
    这是一个狗类
    """
    # python中的构造函数，用于实例时初始化对象，python在构造函数中无法直接访问self，是通过第一个参数传递进来的
    # > 在python中的self就是this
    
    #这个地方也可以声明变量，格外注意，这里声明的是静态变量，和JS的行为不一样，JS在这里定义的是普通实例变量，需要加static关键字才可以定义静态变量
    static_var = "staticVar";

    def __init__(self,name,age):
        # 第一个参数就是创建的对象本身
        self.name = name;
        self.age = age;
    def sit(self):
        #任何函数的第一个参数都会把self传进来，和其他语言很不一样，感觉类似于函数是编程的思想
        """sit
        模拟狗坐下
        """
        print(f"{self.name} is now sitting");

# 创建对象的时候，会自动调用构造函数，将参数从第二个开始传递
# python中创建对象不需要new
new_dog = Dog("Willie",6);
print(new_dog.name,new_dog.age);
# 和js一样，对象的状态可以乱改
new_dog.abc = 123;
print(new_dog.abc);
print(Dog.static_var);# 直接获取类变量

"""
python中也是没有传统意义上的私有变量的，通过变量前加_可以表示这是一个私有变量，但这只是约定。
也可以加两个_，加上__前缀的属性，python也会向外暴露，暴露的属性名为：_类名__属性名，所以严格意义上来讲，这也不是私有变量
注意，python是完全没有真正意义上的私有变量的，js提供了#前缀，但是python是完全没有，这是python设计哲学的一部分，"We are all consenting adults here"。
"""

