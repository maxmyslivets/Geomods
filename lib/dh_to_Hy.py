"""Приведение результатов геометрического нивелирования в систему нормальных высот"""

from math import sin


def dh_to_Hy(B1, g_y1, B2, g_y2, dh, H1):

    y0_1 = 978030*(1+0.005302*(sin(B1)**2)-0.000007*(sin(2*B1)**2))
    y0_2 = 978030*(1+0.005302*(sin(B2)**2)-0.000007*(sin(2*B2)**2))
    print('y0_2-y0_1 =', y0_2-y0_1)
    H2work = H1 + dh
    Hm = (H1 + H2work) /2
    print('Hm =', Hm)

    kym = 1/980000
    print(-kym)

    g_y_m = (g_y1 + g_y2) /2

    b = -kym * (y0_2-y0_1) * Hm + kym * g_y_m * dh
    print('-kym * y0_2-y0_1 =', -kym * (y0_2-y0_1))
    print('b1 =', -kym * (y0_2-y0_1) * Hm)
    print('b2 =', kym * g_y_m * dh)
    print('b=', b)

    return {
        'Поправка b': b,
        'Исправленное превышение': dh+b,
        'Высота следующего пункта': H1+dh+b,
    }
