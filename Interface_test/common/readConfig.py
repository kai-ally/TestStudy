'''
功能描述：读取config.ini文件
编写人：zk
编写日期：2021/03/19

步骤分析：
    1-
    2-
    3-
'''

import configparser
import os
from common.configLog import logger


class ReadConfig(object):

    def __init__(self):
        # 定义config.ini配置文件的文件的路径
        self._conf_path = os.path.dirname(os.path.dirname(__file__)) + r'/config.ini'
        # 定义处理配置文件的对象
        self.conf = configparser.ConfigParser()
        # 打开配置文件，指定编码格式
        self.conf.read(self._conf_path, encoding='utf-8')

    def get_value(self, section, option):
        # 获取指定section下指定option的值
        value = self.conf.get(section, option)
        logger.info(f'获取{section}下{option}的值为：{value}')
        return value


if __name__ == '__main__':
    rc = ReadConfig()
    rc.get_value('mysql', 'ip')

