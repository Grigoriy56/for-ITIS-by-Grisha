import random


class Player(object):
    count = 0
    def __init__(self, name):
        self.name = name
    def hit(self):
        x = random.random() + 0.05
        if x < 0.8:
            return True
        return False

class Game(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def start_game(self):
        while self.p1.count < 11 or self.p2.count < 11:
            for i in range(3):
                if self.p1.hit():
                    self.p1.count += 1
                if self.p1.count > 10:
                    print(f'{self.p1.name} is winner')
                    break
            if self.p1.count > 10:
                break
            for i in range(3):
                if self.p2.hit():
                    self.p2.count += 1
                if self.p2.count > 10:
                    print(f'{self.p2.name} is winner')
                    break
                if self.p2.count > 10:
                    break
a = Player(1)
b = Player(2)
c = Game(a, b)
c.start_game()