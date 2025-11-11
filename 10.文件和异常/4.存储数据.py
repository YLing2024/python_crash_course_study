import json
from pathlib import Path
# python提供了json模块用于处理json数据
path = Path(__file__).parent / "source" / "data.json";
dict = {
    "name": "张三",
    "age": 18,
    "gender": "男"
};
print(dict);
# python的json模块提供了dumps函数用于将python对象转换为json字符串
json_str = json.dumps(dict);
path.write_text(json_str); # 可以将json字符串写入文件

json_str = path.read_text(); # 可以将文件中的json字符串读取为python对象
# python的json模块提供了loads函数用于将json字符串转换为python对象
dict = json.loads(json_str);
print(dict);