from pathlib import Path
import io
# 获取到source目录的路径
path = Path(__file__).parent / "source";
# 下面的代码就可以往write.txt文件中写入文本内容
(path / "write.txt").write_text("写入一段文本内容");
# 写入是纯粹的覆盖，这里写入了两次，后面写入的就会覆盖前面写入的内容
(path / "write.txt").write_text("写入一段新的文本内容");
# path模块提供的write_text没有办法追加内容，如果要追加内容，需要用更底层的io模块，以追加模式打开文件并写入，这里提供简单示例
io.open(path / "write.txt",mode="a", encoding="utf-8").write("追加一段文本内容");
(path / "write2.txt").write_text(
"""
可以像这样写入多行文本
一行
两行
三行
"""
);
# 下面的方法可以判断路径是否存在
print((path / "abc.txt").exists())
