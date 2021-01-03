# coding:UTF-8
# 发送post请求（json）
# 当post请求中body为json类型，有两种方法传递json数据

# 第一种：先导入json模块，用dumps方法转化为json格式
# 访问开源json格式的Post接口： http://httpbin.org/post

import requests, json

url_json = 'http://httpbin.org/post'

payload = {'qq群名': 'Python学习', 'qq号': '123456789'}

# 通过json.dumps()方法将Python中的类型转化为json类型
payload = json.dumps(payload)

re = requests.post(url=url_json, data=payload)
print(re.text)
# 范围的为json类型，可以使用re.json方法查看结果
print(re.json())


# 第二种：使用json参数默认处理成json格式进行传递
url_json = 'http://httpbin.org/post'

payload = {'qq群名': 'Python学习', 'qq号': '111111'}

re = requests.post(url=url_json, json=payload)
print(re.text)
print(re.json())

# headers 请求头
# headers为Python中的字典类型，所以可以支持dict类型的所有操作方式添加headers信息

url_open = 'https://www.wanandroid.com/user/login'

header = {'User-Agent': 'Mozilla/6.0'}
name_pwd = {'username': 'zhangkai', 'password': '123456'}

re = requests.post(url=url_open, data=name_pwd, headers= header)

print(re.text)
print(re.headers)