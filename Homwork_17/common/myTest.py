'''
功能描述：重构unittest中的初始化函数
编写人：zk
编写日期：2021/04/07

步骤分析：
    1-
    2-
    3-
'''

import unittest
import time
from common.driver import Driver


# 对unittest.TestCase进行重构
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 声明driver对象
        cls.dirver = Driver().app_driver()

    def setUp(self) -> None:
        # 重载APP
        self.dirver.launch_app()
        time.sleep(3)

    def tearDown(self) -> None:
        # 关闭APP
        time.sleep(2)
        self.dirver.close_app()


if __name__ == '__main__':
    unittest.main()
