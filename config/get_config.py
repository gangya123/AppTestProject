import yaml
import os


def get_yaml_data():
    # 获取当前.py文件所在的文件夹路径
    file_dir = os.path.dirname(__file__)
    # 将文件夹路径和文件名拼接成完整的路径
    yaml_path = os.path.join(file_dir, "data.yaml")
    # 以读取的方式打开指定的yaml文件
    info = open(yaml_path, "r", encoding="utf-8")
    # 从yaml文件中加载数据，会将yaml文件中所有的数据转化为一个字典
    config_info = yaml.load(info, Loader=yaml.FullLoader)
    return config_info





