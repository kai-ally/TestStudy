'''
4.	文件data.txt内存在以下内容（每行采用逗号分隔)
lucy:21，tom:30
xiaoming:18，xiaohong:15
xiaowang:20，xiaohei:19
输出年龄大于18岁的人名
'''

# f = open('./data.txt','r',encoding='UTF-8')
# content = f.readlines()
# f.close()

#只读方式打开文件，并将文件中内容保存在列表中
with open('./data.txt','r',encoding='UTF-8') as f:
    content = f.readlines()
# print(content)
list01 = []
list02 = []
dict01 = {}
for i in content:
    i = i.strip('\n')   #去除每个元素中的\n
    list01 = i.split('，')       #使用‘，’分割每个元素为一个小列表
    for j in list01:
        list02 = j.split(':')   #使用':'分割
        dict01[list02[0]] = int(list02[1])      #将每个名字和年龄单独组成一个字典
dict02 = {key:value for key,value in dict01.items() if value > 18}      #使用字典推导式生成大于18岁人员的字典
for key in dict02.keys():
    print(f'大于18岁的有{key}')          #遍历key值进行打印


