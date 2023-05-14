# 读取 data目录下的 params.csv 文件
import csv


def get_csv():
    """
    获取csv数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('params.csv', 'r') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    return data


data = get_csv()
print(data)
