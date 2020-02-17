"""
Преобразование эллипсоидальных (геодезических) координат
в трехмерные прямоугольные координаты
"""

from math import cos, sin, sqrt
from module.ellipsoid import WGS84


# Параметры эллипсоида WGS84
a = WGS84.a
b = WGS84.b
e = WGS84.e


print(__doc__)
"""Name = str(input('Имя точки: '))
B = input('B: ').split(' ')
L = input('L: ').split(' ')
H = float(input('H: '))"""


def results(B, L, H):

    print('\nFunction in work...\n')
    print(a, b, e)


results(0, 0, 0)
