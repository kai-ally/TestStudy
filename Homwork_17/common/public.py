'''
功能描述：提供一些公共操作方法，供其他模块使用
编写人：zk
编写日期：2021/04/07

步骤分析：
    1-
    2-
    3-
'''

from common.driver import Driver


class Public(object):

    def __init__(self):
        # 获取driver对象
        self.driver = Driver().app_driver()
        # 获取APP界面尺寸
        self._x = self.driver.get_window_size()['width']
        self._y = self.driver.get_window_size()['height']

    def swipe_right(self):
        # 右滑
        x1 = int(self._x * 0.75)
        x2 = int(self._x * 0.25)
        y = int(self._y * 0.5)
        self.driver.swipe(x1, y, x2, y, 1500)

    def swipe_lift(self):
        # 左滑
        x1 = int(self._x * 0.75)
        x2 = int(self._x * 0.25)
        y = int(self._y * 0.5)
        self.driver.swipe(x2, y, x1, y, 1500)

    def swipe_up(self):
        # 上滑
        x = int(self._x * 0.5)
        y1 = int(self._y * 0.25)
        y2 = int(self._y * 0.75)
        self.driver.swipe(x, y2, x, y1, 1500)

    def swipe_down(self):
        # 下滑
        x = int(self._x * 0.5)
        y1 = int(self._y * 0.25)
        y2 = int(self._y * 0.75)
        self.driver.swipe(x, y1, x, y2, 1500)
