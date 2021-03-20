'''
功能描述：使用unittest编写测试用例
编写人：zk
编写日期：2021/03/18

步骤分析：
    1-
    2-
    3-
'''

from common.configLog import logger
from common.configHttp import ConfigHttp
from common.readExcel import ReadExcel
from common.writeExcel import WriteExcel
import unittest
from ddt import ddt, data, unpack

# 获取经过处理的测试数据
data_list = ReadExcel().readexcel()

# 声明，使用ddt来调用测试数据
@ddt
class TestA(unittest.TestCase):

    @data(*data_list)
    @unpack
    def test_run(self, id, interfaceUrl, name, Method, value, expect, real, status):
        # 获取执行用例后的HTTP实际结果
        re = ConfigHttp(interfaceUrl, Method, value)
        real_code = re.config_http()
        status = 'Fail'
        try:
            self.assertEqual(str(expect), str(real_code))
            status = 'Success'
        finally:
            logger.info(f'用例{id}执行状态：{status}')
            wb = WriteExcel()
            wb.write_excel(id, real_code, status)


if __name__ == '__main__':
    unittest.main(verbosity=2)
