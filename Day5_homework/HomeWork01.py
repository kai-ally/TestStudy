# 1、打印小猫爱吃鱼，小猫要喝水
'''
类名：猫 Cat（）
属性：名称  name
方法：吃 eat（）
     喝 drink（）
'''


class Cat(object):
    def __init__(self, name):
        self.name = name

    def eat(self, foods):
        print(f'{self.name}爱吃{foods}')

    def drink(self, water):
        print(f'{self.name}要喝{water}')


little_cat = Cat('小猫')
little_cat.eat('鱼')
little_cat.drink('水')
