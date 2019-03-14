# -*- coding: cp936 -*-
import openpyxl

wb = openpyxl.load_workbook (r'C:\Users\1\Desktop\python code\Crawler\1.xlsx')
the_list = []

while True:
    info = input('请输入关键字查找： ').upper()#'aaaa-aaaa-aaaa'也能匹配
    if len(info) == 0:
        continue
    count = 0
    sheet = wb.active 
    for line1 in sheet.values:
        print line1
        if None not in line1:
            #单元格为空的行不匹配
            for line2 in line1:
                if info in line2:
                    count += 1
                    print(line1)

    else:
        print('匹配 %s 的数量统计： %s 个条目被匹配' %(info, count))
'''
匹配 AAAA-AAAA-AAAA 的数量统计： 6 个条目被匹配
'''
