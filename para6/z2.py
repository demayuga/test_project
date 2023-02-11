class MYException(Exception):
    def __str__(self):
        return 'Hello! It`s my testing exception!'


def calculate(num_1 : str, num_2 : str)
    if not num_1.isdigit():
        raise ValueError
    elif not num_2.isdigit():
        raise MYException
    else:
        print('OK!')
        
