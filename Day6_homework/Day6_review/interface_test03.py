# 发送post请求（data）
import requests
# 有时候body参数并不是json格式，是key = value 格式

url_open = 'https://www.wanandroid.com/user/login'

name_pwd = {'username': 'zhangkai', 'password': '123456'}

re = requests.post(url=url_open, data=name_pwd)

print(re.text)
print(re.json())
print(re.json()['data']['username'])
if re.json()['data']['username'] == name_pwd['username']:
    print('登录成功')

