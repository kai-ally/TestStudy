'''
功能描述：读取测试数据
编写人：zk
编写日期：2021/03/17

步骤分析：
    1-
    2-
    3-
'''

import xlrd
import os
from common.configLog import logger


class ReadExcel(object):

    def __init__(self):
        """定义基础属性"""
        # 获取测试数据文件的路径
        self.data_path = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        # 使用xlrd打开测试数据文件
        self.workbook = xlrd.open_workbook(self.data_path)
        # 获取该excel中测试数据所在的sheet页
        self.worksheet = self.workbook.sheet_by_index(0)
        # 获取该sheet页中有效数据的行数
        self.num = self.worksheet.nrows
        # 定义一个空数据列表用于存储处理后的测试数据
        self.data_list = []

    def readexcel(self):
        """处理测试数据"""
        # 获取表中第一行数据作为字典的key
        key = self.worksheet.row_values(0)
        logger.info(f'获取字典key成功，为{key}')
        # 循环读取第二行到最后一行数据，获取每一行数据
        for i in range(1, self.num):
            temp_dict = {}
            value = self.worksheet.row_values(i)
            # 使用字典推导式，将第一行数据和后面的每一行数据组成字典
            temp_dict = {key[j]: value[j] for j in range(len(key))}
            # 并将该字典追加至处理完数据的列表中
            self.data_list.append(temp_dict)
        logger.info(f'获取处理后的测试数据列表成功，为{self.data_list}')
        # 返回处理完数据后的数据列表
        return self.data_list


if __name__ == '__main__':
    re = ReadExcel()
    data = re.readexcel()
