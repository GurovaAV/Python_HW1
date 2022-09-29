# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние между ними в 2D пространстве
import math
x_coord_point1 = int(input('Введите координату X первой точки: '))
y_coord_point1 = int(input('Введите координату Y первой точки: '))
x_coord_point2 = int(input('Введите координату X второй точки: '))
y_coord_point2 = int(input('Введите координату Y второй точки: '))
print('Расстояние между точками:', (math.sqrt((x_coord_point2 - x_coord_point1)**2 + (x_coord_point2 - x_coord_point1)**2)))