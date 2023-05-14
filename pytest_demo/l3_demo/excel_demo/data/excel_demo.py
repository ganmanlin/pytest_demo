import os

import openpyxl


def get_excel():
    # 获取工作簿
    ws = openpyxl.load_workbook('params.xlsx')

    # 读取工作表
    sheet = ws.active
    print(sheet)

    # 读取单个单元格
    a1 = sheet['A1'].value
    print(a1)
    c3 = sheet.cell(column=3, row=3).value
    print(c3)

    # 读取多个连续的单元格
    a1_c3 = sheet['A1', 'C3'].value
    print(a1_c3)


get_excel()
