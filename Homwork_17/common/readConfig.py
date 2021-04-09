'''
功能描述：读取配置文件中的配置信息
编写人：zk
编写日期：2021/04/06

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
        # 获取config文件的文件路径
        self._config_path = os.path.dirname(os.path.dirname(__file__)) + r'/config.ini'
        # 获取读取config文件的对象
        self.conf = configparser.ConfigParser()
        # 指定获取配置文件信息的路径和编码
        self.conf.read(self._config_path, encoding='utf-8-sig')

    def get_values(self, sections, options):
        try:
            # 获取指定section下的option的值，并返回
            opt = self.conf.get(sections, options)
            return opt
        except Exception as e:
            # 如果发生异常，将异常信息输出至日志文件中
            logger.info(f"获取options异常,异常原因{e}")


if __name__ == '__main__':
    rc = ReadConfig()
    rc.get_values('mysql', 'ip')
