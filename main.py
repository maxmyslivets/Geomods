from lib import transdeg
from lib.transdeg import str_dms_to_dms, rad_to_str_dms, deg_to_str_dms, str_dms_to_deg, str_dms_to_rad, dms_to_str_dms_chr
from lib import BLHtoXYZ
from lib import XYZtoBLH
from lib import transformXYZ
from lib import transformDeltaXYZ
from lib import BLtoXY_gaus_kruger
from lib import dh_to_Hy


print('\n\tGEOMODS (by Max Myslivets)\nВыберите операцию:')


def menu():
    
    print('\n\n1.', transdeg.__doc__)
    print('2.', BLHtoXYZ.__doc__)    
    print('3.', XYZtoBLH.__doc__)
    print('4.', transformXYZ.__doc__)
    print('5.', transformDeltaXYZ.__doc__)
    print('6.', BLtoXY_gaus_kruger.__doc__)
    print('7.', dh_to_Hy.__doc__)

    print('0. Выход\n\n')

menu()

menuEnter = None
while menuEnter != '0':

    menuEnter = input()

    if menuEnter == '1':

        print('\n\n1.', rad_to_str_dms.__doc__)
        print('2.', deg_to_str_dms.__doc__)    
        print('3.', str_dms_to_deg.__doc__)
        print('4.', str_dms_to_rad.__doc__)
        print('0. Вернуться обратно\n\n')

        menuEnter = input()
        if menuEnter == '1':
            rad = float(input('Введите угол в радианах: '))
            print(dms_to_str_dms_chr(str_dms_to_dms(rad_to_str_dms(rad))))
        
        elif menuEnter == '2':
            deg = float(input('Введите угол в градусах: '))
            print(dms_to_str_dms_chr(str_dms_to_dms(deg_to_str_dms(deg))))

        elif menuEnter == '3':
            str_dms = input("Введите угол в 'градусы минуты секунды': ")
            print(str_dms_to_deg(str_dms))
        
        elif menuEnter == '4':
            str_dms = input("Введите угол в 'градусы минуты секунды': ")
            print(str_dms_to_rad(str_dms))
        
        elif menuEnter == '0':
            menuEnter = None
            menu()
            continue

        else: print('Такого пункта нету в меню')
    
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
    
    elif menuEnter == '6':
        Name = str(input('Имя точки: '))
        B = str_dms_to_dms(input('Геодезическая широта B: '))
        L = str_dms_to_dms(input('Геодезическая долгота L: '))
        BLtoXY_gaus_kruger.BLtoXY_gaus_kruger(B, L)
    
    elif menuEnter == '7':
        B1 = str_dms_to_rad(input('Геодезическая широта B первой точки: '))
        g_y1 = float(input('Аномалия в свободном воздухе (мГал) в первой точке: '))
        B2 = str_dms_to_rad(input('Геодезическая широта B второй точки: '))
        g_y2 = float(input('Аномалия в свободном воздухе (мГал) во второй точке: '))
        dh = float(input('Превышение, м: '))
        H1 = float(input('Отметка первой точки, м: '))

        print(dh_to_Hy.dh_to_Hy(B1, g_y1, B2, g_y2, dh, H1))
    
    else: print('Такого пункта нету в меню')

    
    menu()
