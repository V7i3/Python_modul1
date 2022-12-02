# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def Quarters(number):
    if number == 1:
        return 'x(0; +oo), y(0; +oo)'
    elif number == 2:
        return 'x(-oo; 0), y(0; +oo)'
    elif number == 3:
        return 'x(-oo; 0), y(-oo; 0)'
    elif number == 4:
        return 'x(0; +oo), y(-oo; 0)'
    else:
        return 'ошибка'
    
x = int(input('Введите координатную четверть: '))

print(Quarters(x))