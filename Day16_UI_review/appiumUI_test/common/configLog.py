'''
功能描述：日志模块
编写人：zk
编写日期：2021/03/31

步骤分析：
    1-
    2-
    3-
'''

import logging
import time
import os


class ConfigLog(object):

    def __init__(self):
        self._filepath = os.path.dirname(os.path.dirname(__file__)) + r'/testLogs/'
        self._log_formatter = logging.Formatter(
            '%(asctime)s - '
            '%(levelname)s - '
            '%(name)s - '
            '%(filename)s - '
            '[line: %(lineno)d] - '
            '%(message)s'
        )
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        if not self._logger.handlers:
            self._logger.addHandler(self._get_console_handler())
            self._logger.addHandler(self._get_file_handler())

    def _get_console_handler(self):
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self._log_formatter)
        return ch

    def _get_file_handler(self):
        time_str = time.strftime('%Y-%m-%d', time.localtime())
        logname = self._filepath + time_str + r'_autotest_log.txt'
        fh = logging.FileHandler(logname, mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self._log_formatter)
        return fh

    def get_logger(self):
        return self._logger


logger = ConfigLog().get_logger()

if __name__ == '__main__':
    logger.info("这是一个日志模块的测试数据")
