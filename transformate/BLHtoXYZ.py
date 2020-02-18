"""Преобразование эллипсоидальных (геодезических) координат
в трехмерные прямоугольные координаты"""

from math import cos, sin, sqrt, radians
from module.ellipsoid import WGS84


# Параметры эллипсоида WGS84
a = WGS84.a
e2 = WGS84.e**2

# Точка для тестового решения
point_0 = {
    'Name': 'MEJN',
    'B': ['55', '22', '3.50745'],
    'L': ['28', '49', '53.67669'],
    'H': 158.0621
    }


def BLHtoXYZ(Name, B, L, H):

    print('\nFunction in work...\n')
    
    """Name = str(input('Имя точки: '))
    B = input('Геодезическая широта B: ').split(' ')
    L = input('Геодезическая долгота L: ').split(' ')
    H = float(input('Эллипсоидальная высота H: '))"""

    B = radians(int(B[0]) + int(B[1])/60 + float(B[2])/3600)
    L = radians(int(L[0]) + int(L[1])/60 + float(L[2])/3600)

    print('\nВычисление радиуса кривизны 1-го вертикала N:')
    N = a / sqrt(1-e2*sin(B)**2)
    print('N =', N, 'м')

    print('\nВычисление X:')
    X = (N+H) * cos(B) * cos(L)
    print('X =', X, 'м')

    print('\nВычисление Y:')
    Y = (N+H) * cos(B) * sin(L)
    print('Y =', Y, 'м')

    print('\nВычисление Z:')
    Z = ((1-e2)*N+H) * sin(B)
    print('Y =', Y, 'м\n\n')


    return {
        'Name': Name,
        'N': N,
        'X': X,
        'Y': Y,
        'Z': Z
        }

#print('Result:', BLHtoXYZ(point_0['Name'], point_0['B'], point_0['L'], point_0['H']))