import random


class cat():

    def __init__(self, name):
        self.name = name
        self.satiety = 40
        self.gladness = 50
        self.weight = 5
        self.alive = True

    def to_eat(self):
        print('I will eat')
        self.satiety += 20
        self.gladness += 2
        self.weight += 2

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 4
        self.satiety -= 5

    def to_chill(self):
        print('I want relax')
        self.satiety -= 5
        self.gladness += 3

    def to_play(self):
        print('I will play')
        self.gladness += 1
        self.satiety -= 10
        self.weight -= 1

    def is_alive(self):
        if self.weight <= 1:
            print('You lost a lot of weight')
            self.alive = False
        elif self.weight > 36:
            print('You have a lot of weight')
            self.alive = False
        elif self.satiety < 1:
            print('You starved to death')
            self.alive = False
        elif self.gladness > 800:
            print('You are very happy cat')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Weight = {self.weight}')
        print(f'Satiety = {self.satiety}')


    def life(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')
        life_choice = random.randint(1, 4)

        if life_choice == 1:
            self.to_eat()
        elif life_choice == 2:
            self.to_sleep()
        elif life_choice == 3:
            self.to_chill()
        else:
            self.to_play()

        self.end_of_day()
        self.is_alive()

barcik = cat(name='Barcik')

for day in range(365):
    if not barcik.alive:
        break
    barcik.life(day)
else:
    print("End of the year!")

