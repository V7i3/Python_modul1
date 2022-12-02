# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

def DistanceCoordinates(x1, y1,x2, y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**0.5

distance = DistanceCoordinates(float(input('x1: ')), float(input('y1: ')), float(input('x2: ')), float(input('y1: ')))
print('Расстояние между двумя точками = ', round(distance, 2))