'''
功能描述：excel写入模块
编写人：zk
编写日期：2021/03/18

步骤分析：
    1-
    2-
    3-
'''

import xlrd
import os
from xlutils.copy import copy
from common.configLog import logger


class WriteExcel(object):

    def __init__(self):
        # 定义测试数据文件所在的文件路径
        self.file_path = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        # 打开指定测试数据文件
        self.workbook = xlrd.open_workbook(self.file_path)
        # 将该文件复制一份，用于写入
        self.w_book = copy(self.workbook)
        # 选择指定的sheet页用于写入
        self.w_sheet = self.w_book.get_sheet(0)

    def write_excel(self, id, realcode, status):
        # 传入坐标值和要写入的值，写入excel文件
        self.w_sheet.write(int(id), 6, realcode)
        self.w_sheet.write(int(id), 7, status)
        # 写入完成后，保存覆盖原文件
        self.w_book.save(self.file_path)
        logger.info('测试数据写入成功')


if __name__ == '__main__':
    wb = WriteExcel()
    wb.write_excel(4, '测试')