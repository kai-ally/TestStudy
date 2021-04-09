'''
功能描述：读取测试数据，供测试用例使用
编写人：zk
编写日期：2021/04/07

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
        # 定义测试数据文件的路径
        self._data_path = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        # 获取工作表的对象
        self.workbook = xlrd.open_workbook(self._data_path)
        # 指定工作的sheet页
        self.worksheet = self.workbook.sheet_by_index(0)
        # 获取有效的最大行数
        self.num_rows = self.worksheet.nrows

    def read_excel(self, classname, methodname):
        # 获取第一行数据作为key值
        keys = self.worksheet.row_values(0)
        # 循环读取每一行数据，与第一行组成字典
        for i in range(1, self.num_rows):
            values = self.worksheet.row_values(i)
            temp_dict = {keys[j]: values[j] for j in range(len(keys))}
            # 判断，该数据是否为所需数据，是，则返回该测试数据中testdata的value值
            if temp_dict['classname'] == classname and temp_dict['methodname'] ==methodname:
                return temp_dict['testdata']
        else:
            # 如果循环结束仍未找到符合条件的数据，则输出日志
            logger.info('未能获取到testData数据')


if __name__ == '__main__':
    rd = ReadExcel()
    # rd.read_excel('ms', 'ab')
    data = rd.read_excel('LittleMessageTest', 'test_normal_message')
    print(data)