"""Вычисление прямоугольных координат Гаусса-Крюгера по геодезическим"""

from lib.transdeg import dms_to_rad, rad_to_str_dms, str_dms_to_dms, deg_to_rad, rad_to_dms
from math import cos, sin


def BLtoXY_gaus_kruger(B, L):
    """Вычисление прямоугольных координат Гаусса-Крюгера по геодезическим"""
    
    print('Вычисляем радиус кривизны первого вертикала:')
    N = 6399698.902-(21562.267-(108.973-0.612*cos(dms_to_rad(B))**2)*cos(dms_to_rad(B))**2)*cos(dms_to_rad(B))**2
    print('N =', N)

    print('Вычисляем коэффициенты a0, a3, a4, a5, a6:')
    a0 = 32140.404-(135.3302-(0.7092-0.0040*cos(dms_to_rad(B))**2)*cos(dms_to_rad(B))**2)*cos(dms_to_rad(B))**2
    a3 = (0.3333333+0.001123*cos(dms_to_rad(B))**2)*(cos(dms_to_rad(B))**2)-0.1666667
    a4 = (0.25+0.00252*cos(dms_to_rad(B))**2)*(cos(dms_to_rad(B))**2)-0.04166
    a5 = 0.0083-(0.1667-(0.1968+0.0040*cos(dms_to_rad(B))**2)*cos(dms_to_rad(B))**2)*cos(dms_to_rad(B))**2
    a6 = (0.166*(cos(dms_to_rad(B))**2)-0.084)*cos(dms_to_rad(B))**2

    print('a0 =', a0, '\na3 =', a3, '\na4 =', a4, '\na5 =', a5, '\na6 =', a6)

    def dms_to_s(dms):

        if dms[0] >= 0:
            s = dms[0]*3600 + dms[1]*60 + dms[2]
        if dms[0] < 0:
            dms[0] = -dms[0]
            s = dms[0]*3600 + dms[1]*60 + dms[2]
            s = -s
        
        return s
    
    L0 = str_dms_to_dms(input("Введите долготу осевого меридиана, например '21 00 00.00000':\n"))

    print('Вычисляем l:')
    l = (dms_to_s(L)-dms_to_s(L0)) / 206265
    print('l =', l)

    print('Вычисляем прямоугольные координаты Гаусса-Крюгера:')
    x = round((6367558.4969 * (dms_to_s(B)/206265)-(a0-(0.5+(a4+a6*l**2)*l**2)*(l**2)*N)*sin(dms_to_rad(B))*cos(dms_to_rad(B))), 4)
    y = round(((1+(a3+a5*l**2)*l**2)*l*N*cos(dms_to_rad(B))), 4)
    print('x =', x, '\ny =', y)

    return [x, y]
