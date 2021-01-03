# session 关联接口

# 使用session完成登录，通过session函数可以自动携带上次请求返回的cookie信息，发送第二次post请求

import requests

url_open = 'https://www.wanandroid.com/user/login'

name_pwd = {'username': 'zhangkai', 'password': '123456'}

s = requests.session()
# 用户登录，登录完成后将cookie存入session对象中
s.post(url=url_open, data=name_pwd)
# 通过session对象发送post请求，会自动携带cookie完成本次请求
re = s.post('https://www.wanandroid.com/lg/todo/list/0')

print(re.text)

if re.text.find('test002') != -1:
    print('待办清单进入成功')

# json数据的处理

# 当请求的参数格式为json格式时，需要导入json模块进行处理
# 一般返回的数据也是json格式，我们处理时往往只需要提取其中几个关键的参数就可以，这时候需要使用json来解析返回的数据

# 使用json包
'''
import json
json.dunmps()  将Python对象编码成JSON字符串 ---encode编码
json.loads()   将已编码的JSON字符串解码为Python对象  ---decode编码  
'''
import json
# help(json)

data_python = {'yoyo': 'True', 'json': 'False', 'python': '23125'}
print(type(data_python))        # <class 'dict'>
data_json = json.dumps(data_python)
print(type(data_json))      # <class 'str'>
print(data_python)      # {'yoyo': 'True', 'json': 'False', 'python': '23125'}
print(data_json)        # {"yoyo": "True", "json": "False", "python": "23125"}

url_home = 'http://www.kuaidi.com/'
url_kuaidi = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-3517000465309-yunda-UUCAO1609422953467.html'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
s = requests.session()
s.get(url=url_home)
re = s.post(url=url_kuaidi, headers=header)
print(re.json())




