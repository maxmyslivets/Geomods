from lib import BLHtoXYZ
from lib import XYZtoBLH
from lib import transformXYZ
from lib import transformDeltaXYZ
from lib import BLtoXY_gaus_kruger
from lib.transdeg import str_dms_to_dms


print('\n\tGEOMODS (by Max Myslivets)\nВыберите операцию:')


def menu():
    
    print('\n\n1.', BLHtoXYZ.__doc__)    
    print('2.', XYZtoBLH.__doc__)
    print('3.', transformXYZ.__doc__)
    print('4.', transformDeltaXYZ.__doc__)
    print('5.', BLtoXY_gaus_kruger.__doc__)

    print('0. Выход\n\n')

menu()

menuEnter = None
while menuEnter != '0':

    menuEnter = input()
    
    if menuEnter == '1':
        Name = str(input('Имя точки: '))
        B = input('Геодезическая широта B: ').split(' ')
        L = input('Геодезическая долгота L: ').split(' ')
        H = float(input('Эллипсоидальная высота H: '))
        print('Result:', BLHtoXYZ.BLHtoXYZ(Name, B, L, H), '\n')
    
    elif menuEnter == '2':
        Name = str(input('Имя точки: '))
        N = float(input('Радиус кривизны 1-го вертикала N: '))
        X = float(input('X: '))
        Y = float(input('Y: '))
        Z = float(input('Z: '))
        print('Result:', XYZtoBLH.XYZtoBLH(Name, N, X, Y, Z), '\n')
    
    elif menuEnter == '3':
        print('In real time this module don\'t work')
    
    elif menuEnter == '4':
        print('In real time this module don\'t work')
    
    elif menuEnter == '5':
        Name = str(input('Имя точки: '))
        B = str_dms_to_dms(input('Геодезическая широта B: '))
        L = str_dms_to_dms(input('Геодезическая долгота L: '))
        BLtoXY_gaus_kruger.BLtoXY_gaus_kruger(B, L)

    
    menu()
