# 携带cookie发送请求

# 共有四种携带cookie的方法

# 方法1：手动获取上一次请求的cookie来设置下次请求的cookie

import requests

url_login = 'https://www.wanandroid.com/user/login'
url_todo = 'https://www.wanandroid.com/lg/todo/list/0'

name_pwd = {'username': 'zhangkai', 'password': '123456'}

re1 = requests.post(url=url_login, data=name_pwd)
cookie = re1.cookies

re2 = requests.get(url=url_todo, cookies=cookie)
print(re2.text)

# 方法二：通过requests.session()自动设置cookie

s = requests.session()
s.post(url=url_login, data=name_pwd)
re = s.get(url=url_todo)
if re.text.find('test002') != -1:
    print('成功')


# 方法三：通过定制cookie，单独设置cookie来访问目标网址

re = requests.post(url=url_login, data=name_pwd)
print(re.cookies['JSESSIONID'])
cookie = {
    'JSESSIONID': re.cookies['JSESSIONID']
}

r2 = requests.get(url=url_todo, cookies=cookie)
print(r2.text)


# 方法四：通过定制cookie，放入header来访问目标网址

re = requests.post(url=url_login,data=name_pwd)
header = {
    'cookie': 'JSESSIONID='+re.cookies['JSESSIONID']
}
r = requests.get(url=url_todo, headers=header)
if r.text.find('已完成清单') != -1:
    print('成功')