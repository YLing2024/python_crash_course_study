# 定义父类
class Animal:
    animalCount = 0;# 这里定义的是静态变量，不依赖任何实例，可以直接通过Animal.animalCount访问
    # 实际上，下面的方法都是静态方法，他们的实例状态是通过self传递实现的，你可以通过Animal.__init__访问到构造函数。

    def __init__(self,name,age,**kParams):
        super().__init__(**kParams);
        Animal.animalCount += 1;# 每次实例化让动物数量加一
        self.name = name;
        self.age = age;

    def make_sound(self):
        print("I am",self.name,self.age);

# 定义父类
class Runnable:
    # 这里注意，由于super是动态的，我们完全不知道super是什么，所以通过两个*来透传值
    def __init__(self,**kParams):
         super().__init__(**kParams); # 这里**是解包，将kParams中的值解包出来，作为命名参数传递，如果是一个*，就是用来解构可迭代对象的。

    def run(self):
        print(self.name,"is running");

#定义子类，括号里面是基类，python支持多继承
class Dog(Runnable,Animal):
    def __init__(self,age):
        # 子类里面，通过super()可以拿到父类，这类调用父类的构造函数来参与构造
        # 这里的super()拿到的其实并不是父类，究其本质，拿到的是MRO列表中下一个类，可以通过 类名.mro() 来查看指定类的mro结构
        # MRO列表顺序原则
        # 1. 子类一定在所有父类之前
        # 2. 父类按照继承声明顺序排序
        # 3. 父类内部的MRO不会被打断，即继承顺序不变
        # 4. 如果出现循环继承，直接报错
        super().__init__(name = "Dog",age = age);
    
    def sayHello(self):
        print("Hello, I am",self.name,self.age);

    # 子类重写父类方法
    def make_sound(self):
        print("I am a dog");


dog = Dog(
    age=123
);
dog.run();
dog.sayHello();
dog.make_sound();
# 既然都是静态方法，我们自然可以通过类直接调用，但此时self就必须手动传递了
Animal.make_sound(dog);

# 补充一下解包语法

map = {
    "a":1,
    "b":2,
    "c":3,
}
map2 ={
    # 键值对的解包需要**
    **map,
    "d":4,
}
print(map2)

list1 = [1,2,3,4];
list2 = [
    *list1, # 列表的解包需要*
    5,
    6,
    7,
]
print(list2)

# 和js差不多，解包后可以用于字面量创建，也可以用于函数调用，键值对解包后可以作为命名参数的传递，列表解包后作为位置参数的传递。