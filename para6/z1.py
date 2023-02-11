try:
    number = int(input('Введіть число: '))
    print(int(100 / number))
except ValueError:
    print('Ви вели не число')
except ZeroDivisionError:
    print('Ділити на нуль не можно')
else:
    print('Помилок не має')
finally:
    print('Кінець!')



