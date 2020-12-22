"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
"""
'''
类名： 人
属性：姓名 name   体重  weight   减肥后的体重
方法： 跑步 run（）  跑一次  体重减去0.5
      吃东西  eat（）  吃一次  体重加1
'''


class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.remain_weight = weight

    def run(self):
        self.remain_weight -= 0.5
        print(f'{self.name}跑步一次，减肥0.5公斤，现在体重{self.remain_weight}')

    def eat(self):
        self.remain_weight += 1
        print(f'{self.name}每次吃东西胖1公斤，现在体重{self.remain_weight}')

    def __str__(self):
        return f'{self.name}爱跑步，也爱吃东西'


xiaoming = Person('小明', 75)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
xiaoming.run()

xiaomei = Person('小美', 45)
print(xiaomei)
xiaomei.run()
xiaomei.eat()
xiaomei.run()
