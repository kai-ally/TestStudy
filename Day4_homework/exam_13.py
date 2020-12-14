'''
13、开发一个注册系统，保存用户名和密码，存在的用户提示已注册，不存在的可以注册成功
'''

glo_userlist = []       #定义用户列表为全局变量
def main_GUI():
    '''界面-用户注册'''
    global glo_userlist     #声明使用全局变量
    print('*'*25)
    print('*******用户注册*******')
    name = input('请输入你要注册的用户名：')
    pwd = input('请输入您的密码：')
    #判断用户列表长度，如何为空，则直接添加
    if len(glo_userlist) == 0:
        add_user(name,pwd)
    else:
        #不为空时则跳转至检查用户函数
        n = check_user(name,pwd)
        #接收返回值，并判断：如何返回值为0，则说明该用户未注册，则对该用户进行添加
        if n == 0:
            add_user(name,pwd)
        else:
            #如果返回值不为0，则意味着该用户存在，返回主界面，重新注册
            main_GUI()

def add_user(name,pwd):
    '''添加用户至列表'''
    #声明全局变量
    global glo_userlist
    #定义一个空字典
    l_dict = {}
    #向字典中录入用户名和密码
    l_dict['name'] = name
    l_dict['passworld'] = pwd
    #追加该字典至用户列表中进行存储
    glo_userlist.append(l_dict)
    print('用户注册成功')
    #注册成功后，返回主页面进行下一次注册
    main_GUI()

def check_user(name,pwd):
    '''检查用户是否存在'''
    global glo_userlist
    #遍历用户列表，如果存在则提示用户已注册，并跳出循环
    for i in glo_userlist:
        if i['name'] == name:
            print('该用户已注册')
            break
    else:
        #如果遍历整个用户列表，无该用户，则返回0
        return 0

if __name__ == '__main__':
    main_GUI()