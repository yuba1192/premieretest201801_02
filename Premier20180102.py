# -*- coding: utf-8 -*-
import xlrd
FILE = 'data.xlsx'
book = xlrd.open_workbook(FILE)
s = book.sheet_by_name('students')

aa = s.ncols
for j in range(s.nrows - 2):
    if j == 0:
        ss = "名前　　　　　"
        for i in range(s.ncols - 3):
            ss = ss + str(s.cell_value(2 + j, 3 + i)) + "　"
        ss = ss + "合計点"
        print(ss)
    else:
        ss = ""
        count = 0
        for i in range(s.ncols - 1):
            if i == 0:
                ss = ss + str(s.cell_value(2 + j, 1 + i)) + "　"
            elif i == 1:
                if len(str(s.cell_value(2 + j, 1 + i))) == 1:
                    ss = ss + str(s.cell_value(2 + j, 1 + i)) + "　　　"
                elif len(str(s.cell_value(2 + j, 1 + i))) == 2:
                    ss = ss + str(s.cell_value(2 + j, 1 + i)) + "　　"
                else:
                    ss = ss + str(s.cell_value(2 + j, 1 + i)) + "　"
            else:
                ss = ss + str(int(s.cell_value(2 + j, 1 + i))) + "　　"
                count = count + int(s.cell_value(2 + j, 1 + i))
        ss = ss + str(count)
        print(ss)
