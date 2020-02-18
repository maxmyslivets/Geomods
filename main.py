from module import radToDms
from transformate import BLHtoXYZ
from transformate import XYZtoBLH
from transformate import transformXYZ
from transformate import transformDeltaXYZ


print('\n\tGEOMODS (by Max Myslivets)\nВыберите операцию:')


def menu():
    
    print('\n\n1.', radToDms.__doc__)
    print('2.', BLHtoXYZ.__doc__)    
    print('3.', XYZtoBLH.__doc__)
    print('4.', transformXYZ.__doc__)
    print('5.', transformDeltaXYZ.__doc__)

    print('0. Выход\n\n')

menu()

menuEnter = None
while menuEnter != '0':

    menuEnter = input()

    if menuEnter == '1':
        print('Введите угол в радианах:')
        rad = float(input())
        print(radToDms.dms(rad))
    
    elif menuEnter == '2':
        Name = str(input('Имя точки: '))
        B = input('Геодезическая широта B: ').split(' ')
        L = input('Геодезическая долгота L: ').split(' ')
        H = float(input('Эллипсоидальная высота H: '))
        print('Result:', BLHtoXYZ.BLHtoXYZ(Name, B, L, H), '\n')
    
    elif menuEnter == '3':
        Name = str(input('Имя точки: '))
        N = float(input('Радиус кривизны 1-го вертикала N: '))
        X = float(input('X: '))
        Y = float(input('Y: '))
        Z = float(input('Z: '))
        print('Result:', XYZtoBLH.XYZtoBLH(Name, N, X, Y, Z), '\n')
    
    elif menuEnter == '4':
        print('In real time this module don\'t work')
    
    elif menuEnter == '5':
        print('In real time this module don\'t work')

    
    menu()
