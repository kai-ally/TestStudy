'''
功能描述：驱动appium操作APP执行测试用例
编写人：zk
编写日期：2021/04/03

步骤分析：
    1-
    2-
    3-
'''


from appium import webdriver
import time
from selenium.webdriver.common.by import By


class AppDriver(object):

    def __init__(self):
        self._desire_caps = {
            "deviceName": "MQS7N19403034263",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self._desire_caps)

    def test_app(self):
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/cnf').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/cf7').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'com.ss.android.article.news:id/c0h').click()
        time.sleep(5)


if __name__ == '__main__':
    ad = AppDriver()
    ad.test_app()

