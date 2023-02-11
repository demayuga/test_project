class Processor:
    def calculate(self):
        print('Calculate...')

    def __init__(self):
        super().__init__()
        self.core_count = 4


class Display:
    def display(self):
        print('Display image...')

    def __init__(self):
        super().__init__()
        self.resolution = 120


class SmartPhone(Processor, Display):
    def print_all(self):
        print('I have processor and display')
        print(self.resolution)
        print(self.core_count)


iphone = SmartPhone()
iphone.print_all()