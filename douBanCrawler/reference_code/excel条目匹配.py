# -*- coding: cp936 -*-
import openpyxl

wb = openpyxl.load_workbook (r'C:\Users\1\Desktop\python code\Crawler\1.xlsx')
the_list = []

while True:
    info = input('������ؼ��ֲ��ң� ').upper()#'aaaa-aaaa-aaaa'Ҳ��ƥ��
    if len(info) == 0:
        continue
    count = 0
    sheet = wb.active 
    for line1 in sheet.values:
        print line1
        if None not in line1:
            #��Ԫ��Ϊ�յ��в�ƥ��
            for line2 in line1:
                if info in line2:
                    count += 1
                    print(line1)

    else:
        print('ƥ�� %s ������ͳ�ƣ� %s ����Ŀ��ƥ��' %(info, count))
'''
ƥ�� AAAA-AAAA-AAAA ������ͳ�ƣ� 6 ����Ŀ��ƥ��
'''
