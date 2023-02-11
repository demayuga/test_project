class Student():
    print('Hi')
    count_students = 0

    def __str__(self):
        return f'Hi!I`m student! My name is {self.name}. My height is {self.height}'

    def __del__(self):
        print('I`m go to sleep')

    def __init__(self, height=165, name = None):
        self.height = height
        self.name = name
        Student.count_students += 1

    def say_my_height(self):
        print(f'Hi my height is {self.height}')

    def say_hi(self):
        print('Hi')


nick = Student()
kate = Student(height=150, name='Kate')
bob = Student(height=180, name='Bob')

kate.say_my_height()
kate.say_hi()

print(kate)
