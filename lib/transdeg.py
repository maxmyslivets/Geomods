"""Преобразование угловых мер"""

# deg_to_rad: градусы >> радианы
# rad_to_dms: радианы >> [градусы, минуты, секунды]
# deg_to_dms: градусы >> [градусы, минуты, секунды]
# rad_to_deg: радианы >> градусы
# dms_to_rad: [градусы, минуты, секунды] >> радианы
# dms_to_deg: [градусы, минуты, секунды] >> градусы
# str_dms_to_dms: 'градусы минуты секунды' >> [градусы, минуты, секунды]
# dms_to_str_dms: [градусы, минуты, секунды] >> 'градусы минуты секунды'
# rad_to_str_dms: радианы >> 'градусы минуты секунды'
# deg_to_str_dms: градусы >> 'градусы минуты секунды'
# str_dms_to_deg: 'градусы минуты секунды' >> градусы
# str_dms_to_rad: 'градусы минуты секунды' >> радианы
# dms_to_str_dms_chr: [градусы, минуты, секунды] >> 'градусы минуты секунды' с символами

from math import radians, degrees, trunc


def deg_to_rad(deg):
    """градусы >> радианы"""

    return radians(deg)


def rad_to_dms(rad):
    """радианы >> [градусы, минуты, секунды]"""

    deg = degrees(rad)
    dms = deg_to_dms(deg)

    return dms


def deg_to_dms(deg):
    """градусы >> [градусы, минуты, секунды]"""

    if deg >= 0:
        d = trunc(deg)
        m = trunc((deg - d) * 60)
        s = round(((((deg - d) * 60)-trunc((deg - d) * 60)) * 60), 5)
        dms = [d, m, s]
    
    elif deg < 0:
        deg = -deg
        d = trunc(deg)
        m = trunc((deg - d) * 60)
        s = round(((((deg - d) * 60)-trunc((deg - d) * 60)) * 60), 5)
        dms = [-d, m, s]

    return dms


def rad_to_deg(rad):
    """радианы >> градусы"""

    return degrees(rad)


def dms_to_rad(dms):
    """[градусы, минуты, секунды] >> радианы"""

    rad = radians(dms_to_deg(dms))
    
    return rad


def dms_to_deg(dms):
    """[градусы, минуты, секунды] >> градусы"""

    if dms[0] >= 0:
        deg = dms[0] + dms[1]/60 + dms[2]/3600
    if dms[0] < 0:
        dms[0] = -dms[0]
        deg = dms[0] + dms[1]/60 + dms[2]/3600
        deg = -deg
    
    return deg


def str_dms_to_dms(str_dms):
    """'градусы минуты секунды' >> [градусы, минуты, секунды]"""

    dms = str_dms.split(' ')
    dms[0] = int(dms[0])
    dms[1] = int(dms[1])
    dms[2] = float(dms[2])

    return dms

def dms_to_str_dms(dms):
    """[градусы, минуты, секунды] >> 'градусы минуты секунды'"""

    def st(n):
        n = str(n)
        if len(n) == 1 or n[1] == '.':
            n = '0'+n
        return n
    
    return (str(dms[0]) + ' ' + st(dms[1]) + ' ' + st(dms[2]))


def rad_to_str_dms(rad):
    """радианы >> 'градусы минуты секунды'"""

    return dms_to_str_dms(rad_to_dms(rad))


def deg_to_str_dms(deg):
    """градусы >> 'градусы минуты секунды'"""

    return dms_to_str_dms(deg_to_dms(deg))


def str_dms_to_deg(str_dms):
    """'градусы минуты секунды' >> градусы"""

    return dms_to_deg(str_dms_to_dms(str_dms))


def str_dms_to_rad(str_dms):
    """'градусы минуты секунды' >> радианы"""

    return radians(str_dms_to_deg(str_dms))


def dms_to_str_dms_chr(dms):
    """[градусы, минуты, секунды] >> 'градусы минуты секунды' с символами"""

    def st(n):
        n = str(n)
        if len(n) == 1 or n[1] == '.':
            n = '0'+n
        return n
    
    return (str(dms[0]) + chr(730) + ' ' + st(dms[1]) + chr(697) + ' ' + st(dms[2]) + chr(698))
