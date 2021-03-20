'''
功能描述：用于执行测试用例中的http请求
编写人：zk
编写日期：2021/03/18

步骤分析：
    1-
    2-
    3-
'''

import requests
from common.configLog import logger


class ConfigHttp(object):

    def __init__(self, url, Method, value):
        # 定义接收的参数
        self.url = url
        self.method = Method
        self.payload = eval(value)
        self.header = {}
        self.timeout = 10000

    def config_http(self):
        # 对接收的用例数据进行判断，调用不同的http请求的方法
        if self.method.lower() == 'post':
            logger.debug(f'测试链接为{self.url}')
            return self.post_data()
        elif self.method.lower() == 'get':
            logger.debug(f'测试链接为{self.url}')
            return self.get_data()
        elif self.method.lower() == 'put':
            logger.debug(f'测试链接为{self.url}')
            return self.put_data()

    def post_data(self):
        # post方法，返回json数据中error参数值
        re = requests.post(url=self.url, data=self.payload, headers=self.header, timeout=self.timeout)
        logger.info(re.json())
        return re.json()['errorCode']

    def get_data(self):
        # get方法，返回json数据中error参数值
        re = requests.get(url=self.url, params=self.payload, headers=self.header, timeout=self.timeout)
        logger.info(re.json())
        return re.json()['errorCode']

    def put_data(self):
        # put方法，返回json数据中error参数值
        re = requests.put(url=self.url, data=self.payload, headers=self.header, timeout=self.timeout)
        logger.info(re.json())
        return re.json()['errorCode']


if __name__ == '__main__':
    test_data = [{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'zhangkai','password':'123456'}", 'expect': '0', 'real': '0', 'status': 'Success'}, {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'zk03','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '-1', 'status': 'Fail'}, {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'Get', 'value': "{'username':'liangchao'}", 'expect': '0', 'real': '0', 'status': 'Success'}]
    ch = ConfigHttp(test_data[0]['interfaceUrl'], test_data[0]['Method'], test_data[0]['value'])
    ch.config_http()
