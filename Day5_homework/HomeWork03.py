"""
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""

'''
类名：房子
属性：户型     总面积     家具列表   可用面积
方法：放家具    放一次家具，可用面积减去放去家具的面积
    __str__方法  用来打印房子此时的户型、面积、家具列表、可用面积

类名：家具
属性：家具名称    家具的占地面积
'''


class House(object):
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.remain_area = area
        self.f_list = []

    def add_furniture(self, furniture):
        if furniture.size <= self.remain_area:
            self.remain_area -= furniture.size
            self.f_list.append(furniture.name)
            print(f'{furniture.name}放入房子了，剩余面积还有{self.remain_area}')
        else:
            print(f'{furniture.name}放不下了')

    def __str__(self):
        return f'户型：{self.house_type},总面积：{self.area},剩余面积：{self.remain_area},家具列表：{self.f_list}'


class Furniture(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size


bed = Furniture('床', 4)
robe = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

my_house = House('三室两厅', 180)
print(my_house)

my_house.add_furniture(bed)
my_house.add_furniture(robe)
my_house.add_furniture(table)

print(my_house)
