'''
功能描述：Appium复习
编写人：zk
编写日期：2021/03/30

步骤分析：
    1-
    2-
    3-
'''

from appium import webdriver

import time

from selenium.webdriver.common.by import By


class TestAppium(object):

    def __init__(self):
        #  定义设备的连接参数（包括设备的名称、平台、版本、测试app的包名等信息）
        self.desire_caps = {
            "deviceName": "127.0.0.1:21503",
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "appPackage": "com.ss.android.article.news",
            "appActivity": "com.ss.android.article.news.activity.MainActivity",
            "unicodeKeyboard": True,
            "noReset": True
        }
        # 远程连接appium服务器
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desire_caps)

    def testapp(self):
        # 休眠2s，防止代码执行过快，页面刷新过慢
        time.sleep(2)
        # 使用id定位发布按钮，并点击该按钮
        self.tap_button('id', 'com.ss.android.article.news:id/bov')
        time.sleep(2)
        # 使用id定位’发微头条‘按钮并点击
        self.tap_button('id', 'com.ss.android.article.news:id/h7')
        time.sleep(2)
        # 定位输入框，输入要发布的微头条数据
        self.sendkey_button('id', 'com.ss.android.article.news:id/blh', "今天天气不错！！！！！")
        time.sleep(2)
        # 定位发布按钮，将输入的微头条信息进行发布
        self.tap_button('id', 'com.ss.android.article.news:id/a8n')
        time.sleep(2)
        # 调用app的关闭函数
        self.close_app()

    def testapp2(self):
        time.sleep(2)
        self.swipeleft_button()
        time.sleep(2)
        self.swiperight_button()
        time.sleep(2)
        self.swipedown_button()
        time.sleep(2)
        self.close_app()

    def tap_button(self, methold, values):
        """按钮点击方法"""
        # 判断定位方式，使用id定位，并传入资源id的值
        if methold == 'id':
            self.driver.find_element(By.ID, values).click()
        if methold == 'text':
            self.driver.find_element_by_android_uiautomator("new UiSelecter().text(\"发布\")")
        pass

    def sendkey_button(self, methold, values, message):
        """输入框输入内容"""
        if methold == 'id':
            self.driver.find_element(By.ID, values).send_keys(message)
            pass

    def swipeup_button(self):
        """向上滑动"""
        # 获取屏幕大小的坐标值
        x, y = self._get_size()
        # 定义滑动时的横坐标位置
        x1 = int(x * 0.5)
        # 定义滑动时纵坐标的开始和结束的位置
        y1 = int(y * 0.25)
        y2 = int(y * 0.75)
        # 滑动屏幕制定的时间和滑动的方向
        self.driver.swipe(x1, y2, x1, y1, 1000)

    def swipedown_button(self):
        x, y = self._get_size()
        x1 = int(x * 0.5)
        y1 = int(y * 0.25)
        y2 = int(y * 0.75)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipeleft_button(self):
        x, y = self._get_size()
        x1 = int(x * 0.25)
        x2 = int(x * 0.75)
        y1 = int(y * 0.5)
        self.driver.swipe(x2, y1, x1, y1, 1000)

    def swiperight_button(self):
        x, y = self._get_size()
        x1 = int(x * 0.25)
        x2 = int(x * 0.75)
        y1 = int(y * 0.5)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def _get_size(self):
        """获取屏幕的大小"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def close_app(self):
        """关闭app"""
        self.driver.close_app()


if __name__ == '__main__':
    ta = TestAppium()
    # ta.testapp()
    ta.testapp2()