class Human:
    hunger = 100

    def say_hi(self):
        print('Hi')


class Student(Human):
    university = 'CNTU'


class Grandparent:
    height = 170
    satiety = 100
    age = 60




class Parent(Grandparent):
    age = 40


class Child(Parent):
    height = 50
    age = 8


olga = Grandparent
anton = Parent
oleg = Child


class Hello_world:
    var = True

    def __init__(self):
        self.var = False

    def change_car(self):
        self.var = True


class Hi(Hello_world):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)
        super().change_var()
        print(self.var)


hi = Hi()













