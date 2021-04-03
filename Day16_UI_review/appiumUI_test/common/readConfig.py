'''
功能描述：读取config.ini配置文件中的数据
编写人：zk
编写日期：2021/03/31

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
        self._config_path = os.path.dirname(os.path.dirname(__file__)) + r'/config.ini'
        self.conf = configparser.ConfigParser()
        self.conf.read(self._config_path, encoding='utf-8-sig')

    def get_values(self, section, option):
        value = self.conf.get(section, option)
        logger.info(f'读取到{section}下的{option}为：{value}')
        return value


if __name__ == '__main__':
    rc = ReadConfig()
    rc.get_values('mysql', 'port')

