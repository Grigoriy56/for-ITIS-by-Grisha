import random as rd


class Warroir(object):
    dam = 0

    def __init__(self, name='No_name', max_hp=100, hp=100, race=None, gender=None, dodge=0, buff_scale=1):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.race = race
        self.gender = gender
        self.dodge = dodge
        self.buff_scale = buff_scale

    def attack(self, harvest, friend):
        if self.__class__.__name__ != 'Druid' and self.__class__.__name__ != 'Shaman':
            if rd.randint(0, 100) < self.dodge:
                harvest.hp -= self.dam
                print(
                    f'{self.race} {self.__class__.__name__} {self.name} произвёл атаку на {harvest.race} {harvest.__class__.__name__} {harvest.name} с силой {self.dam}')
            else:
                print(
                    f'{self.race} {self.__class__.__name__} {self.name} промахнулся по {harvest.race} {harvest.__class__.__name__} {harvest.name}')
        elif self.__class__.__name__ == 'Druid':
            if rd.randint(0, 100) < 30 and harvest.__class__.__name__ != 'Shaman':
                harvest.hp = 10
                print(
                    f'{self.race} {self.__class__.__name__} {self.name} заразил {harvest.race} {harvest.__class__.__name__} {harvest.name}')
            elif rd.randint(0, 100) < 70:
                if friend.__class__.__name__ != 'Druid':
                    friend.hp = friend.max_hp
                    print(
                        f'{self.race} {self.__class__.__name__} {self.name} вылечил {friend.race} {friend.__class__.__name__} {friend.name}')
        elif self.__class__.__name__ == 'Shaman':
            print('sh')
            if rd.randint(0, 100) < 50 and harvest.__class__.__name__ != 'Druid':
                print(
                    f'{self.race} {self.__class__.__name__} {self.name} заразил {harvest.race} {harvest.__class__.__name__} {harvest.name}')
                harvest.hp = 10

            elif rd.randint(0, 100) < 50:
                if friend.__class__.__name__ != 'Shaman':
                    friend.hp = friend.max_hp
                    print(
                        f'{self.race} {self.__class__.__name__} {self.name} вылечил {friend.race} {friend.__class__.__name__} {friend.name}')

    def bio(self):
        print(self.race, self.gender, self.name, self.hp)


class Human(Warroir):

    def __init__(self, name=None, gender=None):
        super().__init__(name, gender)
        self.buff_scale = 1.1
        self.race = 'Человек'


class Light(Human):
    dam = rd.randint(30, 50)

    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.dodge = (self.dodge + 30) * self.buff_scale
        self.name = name
        self.gender = gender
        self.hp = 200
        self.max_hp = 200


class Hard(Human):
    dam = rd.randint(50, 70)

    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.dodge = 0
        self.name = name
        self.gender = gender
        self.hp = 500
        self.max_hp = 500


class Druid(Human):

    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.dodge = (self.dodge + 70) * self.buff_scale
        self.name = name
        self.gender = gender


class Ork(Warroir):
    buff_scale = 1.1

    def __init__(self, name=None, gender=None):
        super().__init__(name, gender)
        self.race = 'Орк'


class Berserk(Ork):
    dam = rd.randint(60, 90) * Ork.buff_scale

    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.dodge = 10
        self.name = name
        self.gender = gender
        self.hp = 600
        self.max_hp = 600


class Shaman(Ork):

    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.dodge = (self.dodge + 70)
        self.name = name
        self.gender = gender
        self.hp = 120
        self.max_hp = 120


################################


alians = []
orda = []
for i in range(20):
    o = Shaman(i, 'female')
    h = Druid(i, 'female')
    orda.append(o)
    alians.append(h)
for i in range(20, 30):
    o = Berserk(i, 'male')
    h = Hard(i, 'male')
    orda.append(o)
    alians.append(h)
for i in range(30, 50):
    o = Berserk(i, 'male')
    h = Hard(i, 'male')
    orda.append(o)
    alians.append(h)


###############################


def battle(team1, team2):
    def fight(fighter1, fighter2):
        f1 = team1[rd.randint(0, lent1 - 1)]
        f2 = team2[rd.randint(0, lent2 - 1)]
        fighter1.attack(fighter2, f1)
        fighter2.attack(fighter1, f2)
        if fighter2.hp < 1 and fighter1.hp < 1:
            print(
                f'{fighter2.race} {fighter2.__class__.__name__} {fighter2.race} и {fighter1.team} {fighter1.__class__.__name__} {fighter1.name} пали смертью храбрых')
            team1.remove(fighter1)
            team2.remove(fighter2)
        elif fighter2.hp < 1:
            print(f'{fighter2.race} {fighter2.__class__.__name__} {fighter2.race} убит в бою')
            team2.remove(fighter2)
        elif fighter1.hp < 1:
            print(f'{fighter1.race} {fighter1.__class__.__name__} {fighter1.race} убит в бою')
            team1.remove(fighter1)

    lent1 = len(team1)
    lent2 = len(team2)
    while lent1 != 0 or lent2 != 0:
        if lent1 == 0 or lent2 == 0:
            break
        h = team1[rd.randint(0, lent1 - 1)]
        o = team2[rd.randint(0, lent2 - 1)]
        fight(h, o)
        lent1 = len(team1)
        lent2 = len(team2)

    if len(team1) == 0:
        print(team2[0].race, 'победитель!!! Поздравляем!!!!!')
    if len(team2) == 0:
        print(team1[0].race, 'победитель')


battle(alians, orda)
