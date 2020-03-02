"""Трансформирование координат координат из одной
системы отсчета координат в другую систему отсчета координат"""


from numpy import array


# Точка для тестового решения
point_0 = {
    'Name': 'MEJN',
    'X': 3167249.611601,
    'Y': 1723573.358845,
    'Z': 5208363.610622,
    'dX': -337.8347,
    'dY': -184.5970,
    'dZ': 513.5447,
    'wX': 6.382,
    'wY': -11.546,
    'wZ': 0.094,
    'm': 1.000020715
    }

point_0 = {
    'Name': 'MEJN',
    'X': 3167249.611601,
    'Y': 1723573.358845,
    'Z': 5208363.610622,
    'dX': -337.8347,
    'dY': -184.5970,
    'dZ': 513.5447,
    'wX': 6.382,
    'wY': -11.546,
    'wZ': 0.094,
    'm': 0.79256756
    }


def transformXYZ(Name, X, Y, Z, dX, dY, dZ, wX, wY, wZ, m):

    print('\nFunction in work...\n')

    """Name = str(input('Имя точки: '))
    X = float(input('X: '))
    Y = float(input('Y: '))
    Z = float(input('Z: '))
    dX = float(input('dX: '))
    dY = float(input('dY: '))
    dZ = float(input('dZ: '))
    wX = float(input('wX: '))
    wX = float(input('wY: '))
    wX = float(input('wZ: '))
    m = float(input('m: '))"""

    k = array([[X], [Y], [Z]])
    print('\nИсходные координаты:\n', k)

    dk = array([[dX], [dY], [dZ]])
    print('\nСмещение координат:\n', dk)

    w = array(
        [[1, wZ, -wY],
        [-wZ, 1, wX],
        [wY, -wX, 1]]
        )
    print('\nПовороты:\n', w)
    
    k2 = ((1+m)*w).dot(k)+dk

    return k2


print('\nResult:', transformXYZ(
    point_0['Name'],
    point_0['X'],
    point_0['Y'],
    point_0['Z'],
    point_0['dX'],
    point_0['dY'],
    point_0['dZ'],
    point_0['wX'],
    point_0['wY'],
    point_0['wZ'],
    point_0['m']
    ))