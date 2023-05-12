import random


class Student:
    def __init__(self, name):
        self.name = name
        self.eat = 50
        self.meow = 0
        self.sleep = True

    def Guests(self):
        print('Receive guests!')
        self.meow += 0.12
        self.eat -= 5

    def to_sleep(self):
        print('ZZzzzz!')
        self.eat += 3

    def to_chill(self):
        print('Chill time!')
        self.eat += 5
        self.meow -= 0.1

    def is_active(self):
        if self.meow < -0.5:
            print('Boring')
            self.sleep = False
        elif self.eat < 0:
            print('Re-estate')
            self.sleep = False
        elif self.meow > 5:
            print('Calm and quiet time!!!')
            self.sleep = False

    def status(self):
        print(f':Coefficient eaten goodies {self.eat}')
        print(f'Pleasure (meow): {round(self.meow, 2)}')

    def live_a_day(self, day):
        day_str = f'Day {day} of {self.name} life'
        print(f'{day_str:=^50}')
        dice = random.randint(1, 3)
        if dice == 1:
            self.Guests()
        elif dice == 2:
            self.to_sleep()
        elif dice == 3:
            self.to_chill()
        self.status()
        self.is_active()

dmytro = Student(name='Zippy😺')
for day in range(365):
    if dmytro.sleep:
        dmytro.live_a_day(day)
    else:
        break

if dmytro.sleep:
    print('I have still alive')
