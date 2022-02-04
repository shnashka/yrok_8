# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt = 0
        self.cat_eat = 30

    def __str__(self):
        return f'Денег в доме - {self.money}, еда в доме - {self.food}, степень загрезнености  - {self.dirt}, кошачия еда - {self.cat_eat}'

    def more_dirt(self):
        self.dirt += 5


class Man:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return '{}, сытость- {} счастье- {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.fullness += 30
            cprint('{} принял(а) пищю'.format(self.name), color='green')


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def act(self):
        i = randint(1, 5)
        if self.fullness <= 30:
            self.eat()

        if self.house.dirt >= 100:
            self.happiness -= 10
        if self.happiness <= 0:
            cprint(f'{self.name} потрачено', color='red')
        if self.fullness <= 0:
            cprint(f'{self.name} потрачено', color='red')

        elif self.house.money <= 150:
            self.work()
        elif i == 1:
            self.work()
        else:
            self.gaming()

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        cprint('{} работать'.format(self.name), color='green')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint('{} дотка '.format(self.name), color='green')


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def act(self):
        i = randint(1, 6)
        if self.fullness <= 30:
            self.eat()
        if self.house.dirt >= 100:
            self.happiness -= 10
        if self.happiness <= 0:
            cprint('{} потрачено'.format(self.name), color='red')
        if self.fullness <= 0:
            cprint('{} потрачено'.format(self.name), color='red')

        elif self.house.food <= 50:
            self.shopping()
        elif self.house.dirt >= 120:
            self.clean_house()
        elif i == 1:
            self.buy_fur_coat()
        elif i == 2:
            self.clean_house()
        elif i == 3:
            self.shopping()

    def shopping(self):
        if self.house.money >= 100:
            self.house.money -= 100
            self.house.food += 50
            self.house.cat_eat += 50
            self.fullness -= 10
            cprint('{} купила еды'.format(self.name), color='green')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.fullness -= 10
            cprint('{} купила шубу'.format(self.name), color='green')

    def clean_house(self):
        if self.house.dirt >= 100:
            self.house.dirt -= 100
            self.fullness -= 10
            cprint('{} убрала дом'.format(self.name), color='green')


class Cat:

    def __init__(self, name, house):

        self.name = name

        self.house = house
        self.cat_fullness = 30

    def __str__(self):
        return 'кошак  - {}, еда стойкость  на - {}'.format(self.name, self.cat_fullness)

    def eat(self):
        if self.house.cat_eat >= 10:

            self.cat_fullness += 20
            self.house.cat_eat -= 10
            cprint('{} поел'.format(self.name), color='green')
        else:
            cprint('у {} нет еды'.format(self.name), color='red')

    def act(self):
        if self.cat_fullness <= 0:
            cprint(' {} потррачено'.format(self.name), color='red')
            return
        i = randint(1, 4)
        if self.cat_fullness < 20:
            self.eat()
        elif i == 1:
            self.eat()
        elif i == 2:
            self.soil()
        else:
            self.sleep()

    def sleep(self):
        cprint('{} спит '.format(self.name), color='green')
        self.cat_fullness -= 10

    def soil(self):
        self.cat_fullness -= 10
        self.house.dirt += 5
        cprint('{} дерет '.format(self.name), color='green')


class Child(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.need_food = 10

    def act(self):
        dice = randint(1, 4)
        if self.fullness <= 0:
            cprint('{} потрачено'.format(self.name), color='red')
        elif (self.fullness <= 10) or (1 <= dice <= 2):
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 10
            self.fullness += 30
            cprint('{} принял(а) пищю'.format(self.name), color='green')

    def sleep(self):
        self.fullness -= 5
        cprint('{} поспал'.format(self.name), color='green')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
ace = Child(name='эйс', house=home)
cat = Cat(name='рюк', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='yellow')
    # home.more_dirt()
    serge.act()
    masha.act()
    ace.act()
    cat.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(ace, color='cyan')
    cprint(cat, color='cyan')
    cprint(home, color='cyan')
# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
