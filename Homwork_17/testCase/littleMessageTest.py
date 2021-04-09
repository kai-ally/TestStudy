'''
功能描述：测试发布微头条用例
编写人：zk
编写日期：2021/04/07

步骤分析：
    1-
    2-
    3-
'''
import time
import unittest
from selenium.webdriver.common.by import By
from common.configLog import logger
from common.myTest import MyTest
from common.readData import ReadExcel


class LittleMessageTest(MyTest):

    def test_normal_message(self):
        # 获取类的名称
        classname = self.__class__.__name__
        # 获取测试方法的名称
        methodname = self._testMethodName
        re = ReadExcel()
        # 根据类名称和方法名获取测试数据
        test_data = re.read_excel(classname, methodname)
        logger.info(f'获取testdata数据成功，为{test_data}')

        # 点击发布按钮
        self.dirver.find_element(By.ID, 'com.ss.android.article.news:id/cnf').click()
        time.sleep(3)
        # 点击微头条按钮
        self.dirver.find_element(By.ID, 'com.ss.android.article.news:id/cf7').click()
        time.sleep(3)
        # 输入微头条信息，即测试数据
        self.dirver.find_element(By.ID, 'com.ss.android.article.news:id/afy').send_keys(test_data)
        time.sleep(3)
        # 点击发布按钮
        self.dirver.find_element(By.ID, 'com.ss.android.article.news:id/dji').click()
        time.sleep(3)

        # 断言，在该页面中寻找指定元素
        self.assertIn('a', self.dirver.page_source, '未找到发布的微头条数据')


if __name__ == '__main__':
    unittest.main()
