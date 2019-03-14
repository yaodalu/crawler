# -*- coding: utf-8-*-
import openyxl

'''
openpyxl中有三个不同层次的类
Workbook是对工作簿的抽象
Worksheet是对表格的抽象
Cell是对单元格的抽象
'''

#Workbook对象
excel = openyxl.Workbook('hello.xlsx')  #创建
excel = openyxl.load_workbook('abc.xlsx') #读取

'''
属性：
active：获取当前活跃的Worksheet
worksheets：以列表的形式返回所有的Worksheet(表格)
read_only：判断是否以read_only模式打开Excel文档
encoding：获取文档的字符集编码
properties：获取文档的元数据，如标题，创建者，创建日期等
sheetnames：获取工作簿中的表(列表)
'''

'''
方法
get_sheet_names：获取所有表格的名称(新版已经不建议使用，通过Workbook的sheetnames属性即可获取)
get_sheet_by_name：通过表格名称获取Worksheet对象(新版也不建议使用，通过Worksheet[‘表名‘]获取)
get_active_sheet：获取活跃的表格(新版建议通过active属性获取)
remove_sheet：删除一个表格
create_sheet：创建一个空的表格
copy_worksheet：在Workbook内拷贝表格
'''

#Worksheet对象
'''
属性：
title：表格的标题
dimensions：表格的大小，这里的大小是指含有数据的表格的大小，即：左上角的坐标:右下角的坐标
max_row：表格的最大行
min_row：表格的最小行
max_column：表格的最大列
min_column：表格的最小列
rows：按行获取单元格(Cell对象) - 生成器
columns：按列获取单元格(Cell对象) - 生成器
freeze_panes：冻结窗格
values：按行获取表格的内容(数据)  - 生成器
'''

'''
方法
iter_rows：按行获取所有单元格，内置属性有(min_row,max_row,min_col,max_col)
iter_columns：按列获取所有的单元格
append：在表格末尾添加数据
merged_cells：合并多个单元格
unmerged_cells：移除合并的单元格
'''

#Cell对象

'''
属性
row：单元格所在的行
column：单元格坐在的列
value：单元格的值
coordinate：单元格的坐标
'''



