class Human:

    def __init__(self, name='Human'):
        self.name = name

    def __str__(self):
        return f"Hi! My name is {self.name}"

class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers:
            print(f'Names of {self.brand} passengers: ')
            for i in self.passengers:
                print(i)
        else:
            print(f'There are no passengers ib {self.brand}')


anna = Human('Anna')
oleg = Human('Oleg')
audi = Auto('Audi')
bmw = Auto('BMW')

audi.add_passengers(anna)
audi.add_passengers(oleg)
audi.print_passengers()

