import requests

'''
http://demo.open.renren.io/renren-fast/#/login
该开源项目有token返回，但由于登录存在验证码限制，则直接使用token访问首页内容
'''

url_token = 'http://demo.open.renren.io/renren-fast-server/sys/menu/nav'

token = 'b4d61eb30c9fb5c0ebf267af28d9ff21'

sessionid = 'C94474B0440E86D16255F7412F5FBE6D'

t = '1609639796870'

data = {'t': t}

header = {
    'Cookie': 'JSESSIONID='+sessionid,
    'token': token
}

re = requests.get(url=url_token, params=data, headers=header)
print(re.json())
