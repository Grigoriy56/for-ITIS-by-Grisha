class Raspberry(object):
    states = (None, 'flowering', 'green', 'red')
    _state_ = states[0]
    now = 0

    def __init__(self, index):
        self._index_ = index
        self._state_ = self.states[self.now]

    def _grow_(self):
        self.now += 1
        self._state_ = self.states[self.now]

    def is_ripe(self):
        if self._state_ == 'red':
            return 'Raspberry is red'
        return f'not ready, study is {self._state_}'


class RaspberryBush(Raspberry):
    raspberries = []

    def __init__(self, n):
        for i in range(n):
            temp = Raspberry(i)
            self.raspberries.append(temp)

    def grow_all(self):
        # не понял, почему это не работает
        # map(lambda x: x._grow_(), self.raspberries)
        for i in range(len(self.raspberries)):
            temp = self.raspberries[i]
            temp._grow_()
            self.raspberries[i] = temp

    def all_are_ripe(self):
        x = list(filter(lambda y: y._state_ == 'red', self.raspberries))
        return all(x) and x != []

    def give_away_all(self):
        if self.all_are_ripe():
            self.raspberries = []

class Human(object):

    def __init__(self, name, plant):
        self.name = name
        self._plant_ = plant

    def work(self):
        self._plant_.grow_all()

    def harvest(self):
        if self._plant_.all_are_ripe():
            self._plant_.give_away_all()
        else:
            print('Stop! Not now! raspberry is not a rabbit. raspberry need time.')

    @staticmethod
    def knowledge_base():
        print("Продукты (на 10 порций)\
        Творог - 500 г\
        Сметана 25% - 200 г\
        Малина - 400 г + 100 г для украшения и прослойки\
        Овсяное печенье - 300 г\
        Масло сливочное - 200 г\
        Желатин - 30 г\
        Сахар - 130 г + 4 ч. л. в желе\
        Сахар ванильный - 10 г\
        Вода - 300 мл")

malina = RaspberryBush(3)
gr = Human('Rama', malina)
gr.harvest()
gr.work()
gr.work()
gr.work()
gr.harvest()
# print(type(galina))
# print(galina.is_ripe())

print(malina.all_are_ripe())
#print(malina.all_are_ripe())
