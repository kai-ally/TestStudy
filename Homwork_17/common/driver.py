'''
功能描述：定义一个dirver，供其他功能模块使用
编写人：zk
编写日期：2021/04/06

步骤分析：
    1-
    2-
    3-
'''
import time
from common.configLog import logger
from appium import webdriver
from common.readConfig import ReadConfig


class Driver(object):

    def __init__(self):
        # 获取配置文件中需求启动app的信息
        self._rc = ReadConfig()
        self._deviceName = self._rc.get_values('Appium', 'deviceName')
        self._platformName = self._rc.get_values('Appium', 'platformName')
        self._platformVersion = self._rc.get_values('Appium', 'platformVersion')
        self._appPackage = self._rc.get_values('Appium', 'appPackage')
        self._appActivity = self._rc.get_values('Appium', 'appActivity')
        self._noReset = self._rc.get_values('Appium', 'noReset')
        # 获取appium服务器的地址
        self._serverIP = self._rc.get_values('Appium-Server', 'ip')

    def app_driver(self):
        # 组合app启动的配置数据
        desire_caps = {
            # 设备名称
            'deviceName': self._deviceName,
            # 设备系统平台
            'platformName': self._platformName,
            # 系统版本
            'platformVersion': self._platformVersion,
            # 要启动的包名
            'appPackage': self._appPackage,
            # 要启动包的Activity
            'appActivity': self._appActivity,
            # 是否每次启动是都不重置app
            'noReset': self._noReset,
            # 解决中文输入的问题
            'unicodeKeyboard': True,
            # 隐藏手机输入法
            'resetKeyboard': True
        }
        # logger.info(desire_caps)
        # 启动app
        driver = webdriver.Remote(self._serverIP, desire_caps)
        # 休眠6秒
        time.sleep(6)
        logger.info('----APP已经启动------')
        return driver


if __name__ == '__main__':
    dr = Driver()
    dr.app_driver()
