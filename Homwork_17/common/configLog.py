'''
功能描述：日志功能模块，可在其他模块中使用日志进行输出调试
编写人：zk
编写日期：2021/04/06

步骤分析：
    1-
    2-
    3-
'''

import logging
import os
import time


class ConfigLog(object):

    def __init__(self):
        # 定义日志的存储路径
        self._log_path = os.path.dirname(os.path.dirname(__file__)) + r'/logs/'
        # 定义日志的输出格式
        self._log_formatter = logging.Formatter('%(asctime)s '
                                                '- %(name)s'
                                                ' - %(filename)s'
                                                ' - [lineNo: %(lineno)d]'
                                                ' - %(funcName)s'
                                                ' - %(levelname)s'
                                                ' - %(message)s')
        # 获取日志对象
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        # 判断日志句柄是否存在，不存在则添加句柄
        if not self._logger.handlers:
            self._logger.addHandler(self._get_console_handler())
            self._logger.addHandler(self._get_file_handler())

    def _get_console_handler(self):
        # 获取控制台输出对象
        ch = logging.StreamHandler()
        # 设置控制台日志输出得级别
        ch.setLevel(logging.INFO)
        # 设置控制台日志输出得格式
        ch.setFormatter(self._log_formatter)
        return ch

    def _get_file_handler(self):
        # 定义一个时间字符串，用于拼接日志文件名
        time_str = time.strftime('%Y-%m-%d', time.localtime())
        # 拼接日志文件的名称
        log_name = self._log_path + time_str + r'_autotest_logs.txt'
        # 指定日志写入的文件路径、写入方式及编码
        fh = logging.FileHandler(log_name, mode='a', encoding='utf-8')
        # 设置日志存储的格式
        fh.setFormatter(self._log_formatter)
        # 设置日志存储的级别
        fh.setLevel(logging.DEBUG)
        return fh

    def get_logger(self):
        # 定义一个供外部访问的方法，返回日志对象
        return self._logger


logger = ConfigLog().get_logger()


if __name__ == '__main__':
    logger.info('1234')