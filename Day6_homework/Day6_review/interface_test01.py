# 发送get请求
import requests

url_open = 'https://www.wanandroid.com/'

re = requests.get(url=url_open)
# re.text 返回的页面已文本信息显示
print(re.text)


# get请求中带参数
# 请求参数：
# 分析连接https://www.wanandroid.com/article/query?k=安卓
# 请求参数：k=安卓，可以使用字典的形式进行传参 {'k': '安卓'}
# 多个参数格式：{'key1': 'value1', 'key2': 'value2','key3': 'value3'}

url_search = 'https://www.wanandroid.com/article/query'
keyword = {'k': "安卓"}

re = requests.get(url=url_search, params=keyword)
print(re.text)

# content 用法
# 请求百度首页时，使用re.text会发现获取到的内容存在乱码，因为百度首页响应内容含有gzip压缩文件
# 可以使用re.content这个方法可以自动解码gzip和deflate压缩

re = requests.get(url='http://www.baidu.com/')
print(re.text)
print(re.content)

# response返回的内容还有其他很多的信息
'''
--re.status_code   # 响应状态码
--re.content       # 字节方式的响应体，自动为你解码 gzip 和 deflate 压缩
--re.headers       # 以字典对象存储服务器响应头，但这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
--re.json()        # requests中内置的JSON解码器，处理后对应Python的字典形式
--re.url           # 获取url
--re.encoding      # 编码格式
--re.cookies       # 获取response返回的cookie
--re.raw           # 获取返回原始响应体
--re.text          # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
--re.raise_for_status()   # 失败请求（非200响应）则抛出异常
'''

