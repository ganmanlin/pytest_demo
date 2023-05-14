# 读取json文件内容
import json


def get_json():
    with open('params.json', 'r') as f:
        data = json.loads(f.read())
        print(list(data.values()))


get_json()
