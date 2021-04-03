'''
功能描述：复习unittest和ddt的用法
编写人：zk
编写日期：2021/03/31

步骤分析：
    1-
    2-
    3-
'''

import unittest
from ddt import ddt, data, unpack

temp_list = [3, 2, 4, 3]
temp_list2 = [(1, 1), (2, 3)]


@ddt
class ReviewUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("这是所有用例执行前的准备工作")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是所有用例执行结束后的清洗工作")

    def setUp(self) -> None:
        print("每次用例执行前都会执行的准备工作")

    def tearDown(self) -> None:
        print("每次用例执行后都会执行的清洗工作")

    @data(*temp_list)
    def test_run1(self, num):
        self.assertEqual(num, 3)

    @data(*temp_list2)
    @unpack
    def test_run2(self, num1, num2):
        self.assertEqual(num1, num2)

    # def test_run3(self):
    #     self.assertEqual(1, 1)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(ReviewUnittest('test_run3'))
    # print(suite)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
