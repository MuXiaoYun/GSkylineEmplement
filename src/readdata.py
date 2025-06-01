import config
from nodegraph import *

def read_data(data_path=config.datapath):
    # read data from .txt file in datapath
    # the first row is a single number for l
    # followed by data rows
    # each data row has several numbers
    # the first one is id
    # the rest is a list containing all the data of the node
    data = []
    l = -1
    try:
        with open(data_path, 'r') as f:
            for index, line in enumerate(f):
                # 去掉行首行尾的空白字符，并按空格分割
                if index == 0:
                    l = int(line.strip())
                    continue
                parts = line.strip().split()
                if len(parts) > 1:
                    # 第一个元素是ID，其余是数据
                    node_id = int(parts[0])
                    node_data = list(map(float, parts[1:]))
                    data.append(node(node_data, node_id))
    except FileNotFoundError:
        print(f"Error: 文件 {data_path} 未找到。")
    except Exception as e:
        print(f"Error: 读取文件时发生错误 - {e}")
    return data, l
