from pathlib import Path # path标准库里面提供了Path类
import os
# 注意，这里的相对路径是基于执行脚本的执行目录，所以这么写其实是有问题的
# path = Path("./source/匆匆.txt"); 
path = Path(__file__);# __file__是当前脚本的绝对路径
path = path.parent / "source" / "匆匆.txt";# 注意，Path类重载了/运算符，Path类将/运算符视为路径拼接
# path类提供直接提供了读取方法
content = path.read_text(encoding="utf-8")
lines = content.splitlines()# 这个方法可以将字符串按照换行符去分割，返回一个列表
lines2 = content.split(os.linesep); # os模块的linesep属性可以获取当前操作系统的换行符，这样写和上面写是等价的
print(lines)
print(lines2)
# 顺带一提，python中的join方法很特殊，是放在字符串上的
# 不管是dart还是js，join方法都是放在list(Array)实例上的，因为dart和js设计哲学是，对谁操作，就方法。而python则强调数据的纯粹性，python认为这是要通过一个可迭代对象来构造一个字符串，所以就将这个方法提供在字符串上了。
print(os.linesep.join(lines)) # 原文又可以打出来了