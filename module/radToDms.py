"""Преобразование радиан в градусы минуты секунды"""

from math import degrees, trunc


def st(n):

    n = str(n)

    if len(n) == 1 or n[1] == '.':
        n = '0'+n
    
    return n


def dms(r):

    deg = degrees(r)

    if deg >= 0:

        d = trunc(deg)
        m = trunc((deg - d) * 60)
        s = round(((((deg - d) * 60)-trunc((deg - d) * 60)) * 60), 5)

        dms_str = str(d)+' '+st(m)+' '+st(s)
    
    elif deg < 0:

        deg = -deg
        d = trunc(deg)
        m = trunc((deg - d) * 60)
        s = round(((((deg - d) * 60)-trunc((deg - d) * 60)) * 60), 5)

        dms_str = '-'+str(d)+' '+st(m)+' '+st(s)


    return dms_str
