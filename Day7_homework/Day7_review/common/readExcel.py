'''
功能描述：读取testData中的测试数据，供给testCase使用
编写人：zk
编写日期：2021/01/12

步骤分析：
    1-导入xlrd包
    2-打开目标路径下的data文件
    3-确定sheet页
    4-确定所有数据的最大行数作为循环的次数，循环读取文件中的数据，并追加至空列表中，并返回该列表
'''

import xlrd
import os


class ReadExcel(object):
    def __init__(self):
        # 获取文件的父路径
        self.path = os.path.dirname(os.path.dirname(__file__))
        # 拼接出data.xls的路径
        self.data_path = self.path + r'/testData/data.xls'
        # 定义空列表，用于存放从data文件中读取的测试数据
        self.data_list = []

    def read_excel(self):
        # 打开目标的数据文件
        workbook = xlrd.open_workbook(self.data_path)
        # 定位sheet页
        worksheet = workbook.sheet_by_index(0)
        # 循环读取该sheet页中每一行的数据，并存入列表，返回该列表
        for i in range(worksheet.nrows):
            value = worksheet.row_values(i)
            # print(value)
            self.data_list.append(value)
        return self.data_list


if __name__ == '__main__':
    r = ReadExcel()
    print(r.read_excel())
