"""Приведение результатов геометрического
нивелирования в систему нормальных высот"""


from math import sin
import win32com.client
import os.path


def result(B1, g_y1, B2, g_y2, dh, H1):

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

    return [H1+dh+b, y0_2, y0_1, Hm, g_y_m, dh]


dataSet = [0.964311865, 3.6, 0.963456654, 7.6, 5.4053, 133.233]
dataSet_2 = [0.963456654, 7.6, 0.963456654, 8.3, 11.2535, 133.233608]


"""print('\nH2 =', result(
    dataSet[0],
    dataSet[1],
    dataSet[2],
    dataSet[3],
    dataSet[4],
    dataSet[5]
), '\n')

print('\nH2 =', result(
    dataSet_2[0],
    dataSet_2[1],
    dataSet_2[2],
    dataSet_2[3],
    dataSet_2[4],
    dataSet_2[5]
), '\n')"""

"""with open("dataset_1.txt", "r") as ds:
    data = ds.readlines()
    
for line in data:

    if '\n' in line:
        line = line[:-1]
    
    line = line.split(', ')

    for i in range(len(line)):
        if i != 0:
            line[i] = float(line[i])
    
    print(line)"""

v = int(input('Вариант: '))

Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(os.path.abspath('dataset.xlsx'))
sheet = wb.ActiveSheet

sheet.Cells(1, 2).value = v
wb.Save()

for rows in range(5):
    Res = result(
        float(str(sheet.Range('B'+str(rows+4)))),
        float(str(sheet.Range('E'+str(rows+4)))),
        float(str(sheet.Range('B'+str(rows+5)))),
        float(str(sheet.Range('E'+str(rows+5)))),
        float(str(sheet.Range('B'+str(rows+19)))),
        float(str(sheet.Range('C'+str(rows+19))))
    )

    sheet.Cells(str(rows+20), 3).value = Res[0]
    sheet.Cells(str(rows+19), 9).value = Res[1]
    sheet.Cells(str(rows+19), 11).value = Res[2]
    sheet.Cells(str(rows+19), 13).value = Res[3]
    sheet.Cells(str(rows+19), 15).value = Res[4]
    sheet.Cells(str(rows+19), 17).value = Res[5]

for rows in range(5):
    Res = result(
        float(str(sheet.Range('B'+str(rows+11)))),
        float(str(sheet.Range('E'+str(rows+11)))),
        float(str(sheet.Range('B'+str(rows+12)))),
        float(str(sheet.Range('E'+str(rows+12)))),
        float(str(sheet.Range('B'+str(rows+26)))),
        float(str(sheet.Range('C'+str(rows+26))))
    )

    sheet.Cells(str(rows+27), 3).value = Res[0]
    sheet.Cells(str(rows+26), 9).value = Res[1]
    sheet.Cells(str(rows+26), 11).value = Res[2]
    sheet.Cells(str(rows+26), 13).value = Res[3]
    sheet.Cells(str(rows+26), 15).value = Res[4]
    sheet.Cells(str(rows+26), 17).value = Res[5]


wb.Save()
wb.Close()

Excel.Quit()
