from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        self.die_roll = randint(1, self.sides)
        print(self.die_roll)


d4 = Die(4)
d6 = Die()
d8 = Die(8)
d10 = Die(10)
d12 = Die(12)
d20 = Die(20)

'''
for i in range(10):
    d6.roll_die()
for i in range(10):
    d10.roll_die()
for i in range(10):
    d20.roll_die()
'''
