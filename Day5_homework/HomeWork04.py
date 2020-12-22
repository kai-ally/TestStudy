"""
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
"""
'''
类名：枪
属性：枪名   子弹总量   剩余子弹量
方法：发射子弹   发射一次，子弹少一发
     装填子弹   装填可以一次装填多发，但子弹最多不让超出子弹的总
     
类名：士兵
属性：士兵的名字
方法：开枪   开枪调用枪的发射子弹的方法
     装填   装填子弹，传参装填子弹的数量，调用枪装填子弹的方法  
'''


class Gun(object):
    def __init__(self, name, num):
        self.name = name
        self.bullet_num = num
        self.remain_num = num

    def shoot(self):
        if self.remain_num > 0:
            print('fire in the hole')
            self.remain_num -= 1
        else:
            print('没子弹了，赶紧装填')

    def load(self, n):
        number = self.bullet_num - self.remain_num
        if n <= number:
            self.remain_num += n
            print(f'装填成功,已装填{n}颗子弹')
        elif self.remain_num == self.bullet_num:
            print(f'{self.name}子弹已装满,无需再装填...')
        else:
            print(f'{self.name}只需装填{number}颗子弹就可以装满')

    def __str__(self):
        return f'{self.name}子弹总量:{self.bullet_num},剩余弹量:{self.remain_num}'


class Soldiers(object):
    def __init__(self, name):
        self.name = name

    def fire(self, gun):
        gun.shoot()

    def fill(self, gun, n):
        gun.load(n)


ak47 = Gun('AK47', 30)
Ryan = Soldiers('瑞恩')

Ryan.fire(ak47)
Ryan.fire(ak47)
Ryan.fire(ak47)
Ryan.fire(ak47)
print(ak47)
Ryan.fill(ak47, 5)
print(ak47)
Ryan.fill(ak47, 4)
print(ak47)
Ryan.fill(ak47, 1)
print(ak47)
