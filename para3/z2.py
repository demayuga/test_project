import random

class Human:
    def __init__(self, name='Human', job='None',
                 home='None', car='None'):
        self.name = name
        self.job = job
        self.home = home
        self.car = car

        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
        self.job = Job(job_list)

    def eat(self):
        if self.home.food() <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping('fuel')
            else:
                self.to_repair()
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
        if manage == 'fuel':
            print('I bought fuel')
            self.car.fuel += 100
            self.money -= 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Hooray! Delicacies!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness += 10
        self.home.mess += 5

    def to_repair(self):
        self.car.strength += 10
        self.money -= 50

    def days_indexes(self, day):
        day = f'Today the {day} of {self.name} life '
        print(f'{day:=^50}')
        print(f'{self.name} indexes: ')
        print(f'Money - {self.money}')
        print(f'Gladness - {self.gladness}')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        print(f'Car fuel - {self.car.fuel}')
        print(f'Car strength - {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.satiety<0:
            print('Dead...')
            return True
        if self.money < -500:
            print('Bankrupt')
            return False


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home == None:
            print('Settled in the house')
            self.get_home()
        if self.car == None:
            print('I bought new car')
            self.get_car()
        if self.job == None:
            self.job = self.get_jod()
            print(f'I dont have a job, I`m going to get {self.get_job}')
        self.days_indexes(day)

        dice = random.randint(1,4)
        if self.satiety < 20:
            print('I`ll go eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is soo much mess... ")
                self.clean_home()
            else:
                print('let`s  chill')
                self.chill()
        elif self.money < 0:
            print('Let`s work')
            self.work()
        elif self.car.strength < 15:
            print('I need to repair my car')
            self.to_repair()
        if dice == 1:
            print('let`s  chill')
            self.chill()
        elif dice == 2:
            print('Let`s work')
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_home()
        elif dice == 4:
            print('Time for treats')
            self.shopping(manage="delicacies")





class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('This carr can`t move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']




job_list = {
    'Java developer':
        {
            'salary': 50,
            'gladness_less': 10
        },
    'Python developer':
        {
            'salary': 60,
            'gladness_less': 5
        },
    'C++ developer':
        {
            'salary': 70,
            'gladness_less': 15
         }
}

brand_of_car = {
    'BMW': {
        'fuel': 100,
        'consumption': 15,
        'strength': 100

    },
    'Audi': {
            'fuel': 130,
            'consumption': 10,
            'strength': 100
    },
    'Mercedes': {
            'fuel': 75,
            'consumption': 12,
            'strength': 100
    },
    'Porsche': {
            'fuel': 85,
            'consumption': 20,
            'strength': 100
    }

}

nick = Human(name='Nick')

for day in range(1, 8):
    if nick.live(day) == False:
        print("Game over")