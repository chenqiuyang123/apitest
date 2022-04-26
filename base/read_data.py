# -*- coding: utf-8 -*-
# @Time : 2022-04-15 10:21
# @Author : CCC.
# @File : read_data.py
# @Project : pythonProject2


import  os
import yaml
import json
from apitest.base.logger import logger
from configparser import ConfigParser


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr




root_path =os.path.dirname(os.getcwd())

class ReadFile():
    def load_file(self,file_name):
        logger.info("加载%s文件"%file_name)
        try:
            data_file_path =os.path.join(root_path,"data",file_name)
            with open(data_file_path,encoding='utf-8') as f:
                data =yaml.safe_load(f)
        except Exception as ex:
            print(ex)
        else:
            return data
        logger.info("读到数据 ==>>  {} ".format(data))

    def load_json(self, file_name):
        logger.info("加载 {} 文件......".format(file_name))
        try:
            data_file_path = os.path.join(root_path, "data", file_name)
            with open(data_file_path, encoding='utf-8') as f:
                    data = json.load(f)
        except Exception as ex:
            print(ex)
        else:
            return data
        logger.info("读到数据 ==>>  {} ".format(data))


    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))

        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data

data =ReadFile()

