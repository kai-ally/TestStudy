'''
功能描述：读取测试用例中处理的测试数据，根据测试数据中的字段判断使用请求方法
编写人：zk
编写日期：2021/01/12

步骤分析：
    1-导入requests包
    2-接收处理后的测试数据，并存入对象属性当中，便于类方法的调用
    3-判断测试数据中请求方法的字段
        3-1 post 则调用post方法，并获取返回的错误码errorCode
        3-2 get  则调用get方法，并获取返回的错误码errorCode
    4-判断返回的错误码与预期的错误码是否一致，一致返回0，不一致则返回1
'''

import requests


class ConfigHttp(object):

    def __init__(self, data_list):
        # 将传入的用例数据存入类的属性当中，便于类中方法的调用
        self.data_dict = data_list

    def config_http(self):
        # 判断用例数据中“method”字段，从而选择不同的请求方式
        if self.data_dict['Method'].lower() == 'post':
            # 调用对应的请求方式，并接收返回的错误码
            n = self.post_data()
            # 调用判断函数，判断实际的错误码和预期的错误码是否一致，并返回判断结果
            return self.check_code(n)
        elif self.data_dict['Method'].lower() == 'get':
            n = self.get_data()
            return self.check_code(n)

    def post_data(self):
        # 使用Post对测试数据进行请求
        re = requests.post(url=self.data_dict['interfaceUrl'], data=eval(self.data_dict['value']))
        # 获取response中的错误码并返回
        status_code = re.json()['errorCode']
        return status_code

    def get_data(self):
        # 使用get对测试数据进行请求
        re = requests.get(url=self.data_dict['interfaceUrl'], params=eval(self.data_dict['value']))
        # 获取response中的错误码并返回
        status_code = re.json()['errorCode']
        return status_code

    def check_code(self, status_code):
        # 判断实际的错误码和预期的错误码是否一致，一致则返回0，不一致则返回1
        if str(status_code) == str(self.data_dict['expect']):
            return 0
        else:
            return 1


if __name__ == '__main__':
    dict01 = [{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post',
               'value': "{'username':'zhangkai','password':'123456'}", 'expect': '0', 'real': '', 'status': ''}]
    re = ConfigHttp(dict01)
    print(re.config_http())
