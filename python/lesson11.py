# Class классы

# объект класса = объект типа = представитель класса = экземпляр класса

from abc import abstractmethod

# 1 обший класс
class Group:
    #общие элементы
    pupils = True
    school_name = 42
    director = 'Marivanna'

    def __init__(self, title, pupils_count, group_leader): 
        # метод запускаемый в момент присвоения обьекта классу
        # Аргумент self обязателен
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader

    def study(self):  #не функция, а метод. Аргумент self обязателен
        print('sit down and read')

    @abstractmethod
    def move(self):
        pass 
    # показ что метод должен реализовываться в дочернем классе


# 2 классы по иерархии ниже 1. дочерний
class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader) #инициал аргументов род класса
        self.class_room = class_room

    def move(self):
        print('Run fast')

class HighGroup (Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('Go slowly')

class MediumGroup(Group):
    max_age = 13
    min_age = 12


# 3 представители классов 2. Наследуют характеристики классов 2 и 1
first_a = PrimaryGroup('1a', 18, 'MF', 112)
first_b = PrimaryGroup('1b', 20, 'TD', 120)
eleve_a = HighGroup('10b', 15, 'TD')
six_a = MediumGroup('6v', 19, 'VV')



# print(first_a.class_room)
# print(first_b.class_room)
# print(first_a.group_leader)
# print(first_a.title)
# print(first_b.pupils_count)
# print(first_a.pupils)
# print(first_a.min_age)
# print(first_a.max_age)
# print(first_a.building_section)
# print(first_a.director)
# first_a.study()
# first_a.move()

# print(eleve_a.pupils)
# print(eleve_a.min_age)
# print(eleve_a.max_age)
# print(eleve_a.director)
# eleve_a.study()
# eleve_a.move()

