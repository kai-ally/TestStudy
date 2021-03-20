'''
功能描述：日志模块，用于输出调试日志
编写人：zk
编写日期：2021/03/17

模块要点：
    1-format常用格式说明
        %(levelno)s : 打印日志级别的数值
        %(levelname)s : 打印日志级别的名称
        %(pathname)s : 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s : 打印当前执行程序名
        %(funcname)s : 打印日志的当前函数
        %(lineno)d : 打印日志的当前行数
        %(asctime)s : 打印输出日志的时间
        %(thread)d : 打印线程ID
        %(threadName)s : 打印线程名称
        %(process)d : 打印进程的ID
        %(message)s : 打印日志信息
    2-日志的级别
        debug : 打印全部级别的日志
        info : 打印info以上级别的日志
        warning : 打印warning以上级别的日志
        error : 打印error以上级别的日志
        critical : 打印critical级别的日志
        级别排序： critical > error > warning > info > debug
    3-
'''

import logging
import os
import time


class ConfigLog(object):

    def __init__(self):
        # 设置日志格式，使用logging.Formatter对日志格式进行格式化
        self._log_format = logging.Formatter('%(asctime)s - '
                                             '%(levelname)s - '
                                             '%(name)s - '
                                             '%(filename)s - '
                                             '%(funcName)s - '
                                             '[line: %(lineno)d] - '
                                             '%(message)s')
        # 设置日志存储的路径
        self._log_dir = os.path.dirname(os.path.dirname(__file__)) + r'/Log/'
        # 新增logger对象
        self._logger = logging.getLogger()
        # 设置日志的记录级别
        self._logger.setLevel(logging.DEBUG)
        # 判断logger对象的句柄，如果不存在，则添加句柄
        if not self._logger.handlers:
            # 添加控制台输出句柄
            self._logger.addHandler(self._get_console_handler())
            # 添加文件输出句柄
            self._logger.addHandler(self._get_file_handler())

    def _get_console_handler(self):
        # 进行控制台的日志输出
        ch = logging.StreamHandler()
        # 设置控制台日志输出的级别
        ch.setLevel(logging.INFO)
        # 设置控制台日志输出的格式
        ch.setFormatter(self._log_format)
        # 返回控制台对象
        return ch

    def _get_file_handler(self):
        # 生成一个时间字符串，用于拼接日志文件的名称
        time_str = time.strftime('%Y_%m_%d', time.localtime())
        # 凭借日志文件的路径
        file = self._log_dir + time_str + r'_aototest_log.txt'
        # 获取日志文件对象，并设置追加模式写入
        fh = logging.FileHandler(file, mode='a', encoding='utf-8')
        # 设置文件内日志级别
        fh.setLevel(logging.DEBUG)
        # 设置文件内日志格式
        fh.setFormatter(self._log_format)
        # 返回文件对象
        return fh

    def get_logger(self):
        # 设置函数，获取日志对象
        return self._logger


# 设置日志对象，可用于其他模块中日志的输出
logger = ConfigLog().get_logger()

if __name__ == '__main__':
    logger.info('1234')
