"""
Преобразование трехмерных прямоугольных координат в
трехмерные эллипсоидальные (геодезические) координаты
"""


import math as m
from radToDms import dms


# Параметры эллипсоида WGS84
a = 6378137.0000
b = 6356752.3142
e = 0.0818191908

print(__doc__)
Name = str(input('Имя точки: '))
N = float(input('Радиус кривизны 1-го вертикала N: '))
X = float(input('X: '))
Y = float(input('Y: '))
Z = float(input('Z: '))


def results(N, X, Y, Z):

    print('\nFunction in work...\n')

    L = m.atan(Y/X)
    D = m.sqrt(X**2+Y**2)

    print('\tAnalising variable D:')

    if D == 0:

        B = (m.pi/2) * (Z/abs(Z))
        L = 0
        H = Z*m.sin(B) - a*m.sqrt(1 - (e**2)*(m.sin(B)**2))

        print('\tD = 0:\tB =', dms(B), '\tL =', dms(L), '\tH =', H)
    
    else:

        La = abs(m.asin(Y/D))
        if Y<0 and X>0: L = 2*m.pi-La
        elif Y<0 and X<0: L = m.pi+La
        elif Y>0 and X<0: L = m.pi-La
        elif Y>0 and X>0: L = La
        elif Y==0 and X>0: L = 0
        elif Y==0 and X<0: L = m.pi

        print('\tD != 0\n\tL =', dms(L))
    
    print('\n\tAnalising variable Z:')

    if Z == 0:

        B = 0
        H = D - a

        print('\tZ = 0:\tB =', dms(B), '\tL =', dms(L), '\tH =', H)

    else:

        print('\tZ != 0')

        r = m.sqrt(X**2+Y**2+Z**2)
        c = m.asin(Z/r)
        p = ((e**2)*a) / (2*r)

        print('\tr =', r, '\n\tc =', c, '\n\tp =', p)

        print('\n\tRun iterations...\n')
        s1 = 0
        i = 0

        while True:
            
            i += 1
            print('\t--- Iteration №', i, end='\t')

            b = c + s1
            s2 = m.asin((p*m.sin(2*b)) / m.sqrt(1-(e**2)*(m.sin(b)**2)))
            d = abs(s2-s1)

            print('d =', d)

            if d <= 0:

                B = b
                H = D*m.cos(B) + Z*m.sin(B) - a*m.sqrt(1-(e**2)*(m.sin(B)**2))

                break

            else: s1 = s2
    
    L = m.atan(Y/X)

    return 'B = '+str(dms(B))+'\t'+'L = '+str(dms(L))+'\t'+'H = '+str(round(H,4))

print(
    '\n\nPoint `'+Name+'`:\t',
    results(N, X, Y, Z)
    )