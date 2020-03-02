"""
Объект "Эллипсоид"
Пример создания объекта:
el = ellipsoid.WGS84
или
from module.ellipsoid import WGS84
a = WGS84.a
Атрибуты:
a - большая полуось
b - малая полуось
e - эксцентриситет
"""


class WGS84():

    a = 6378137.0000
    b = 6356752.3142
    e = 0.0818191908

class krassovsky():

    a = None
    b = None
    e = None
