'''
功能描述：携带测试数据，进行接口测试
编写人：zk
编写日期：2021/01/12

步骤分析：
    1-导入要使用的包：readExcel，configHttp，unittest，ddt
    2-处理从data.xls中获取的数据，使每一条测试用例数据变为字典格式，所有用例组成一个列表
    3-使用unittest派生类
        3-1 在test_case方法中调用configHttp模块处理测试数据，并获取测试结果
        3-2 使用ddt模块，将所有用例组成的列表逐一传入test_case方法当中进行执行
        3-3 使用断言判定用例执行是否成功
'''

from common.readExcel import *
from common.configHttp import *
import unittest
from ddt import ddt, data, unpack

# 读取data.xls中的数据
t = ReadExcel()
test_data = t.read_excel()
# 定义一个空列表，用来存放处理后字典形式的测试数据
data_list = []
# 外层循环，读取每行有效的测试数据
for j in range(1, len(test_data)):
    temp_dict = {}
    # 内层循环，用来对应第一行表头数据生成字典
    for i in range(len(test_data[0])):
        temp_dict[test_data[0][i]] = test_data[j][i]
    # 将生成的字典存入列表中
    data_list.append(temp_dict)


@ddt
class TestCase(unittest.TestCase):

    # 使用ddt中的data将用例数据列表中的每个字典元素逐一传入test_case函数中
    @data(*data_list)
    # @unpack
    def test_case(self, value):
        # 将每一条用例数据传入ConfigHttp类中进行处理
        r = ConfigHttp(value)
        # print(value)
        # 返回测试执行后的结果
        status_code = r.config_http()
        # 断言，返回为0则用例执行成功，返回非0则用例执行失败
        self.assertEqual(status_code, 0)


if __name__ == '__main__':
    unittest.main()
