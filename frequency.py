import xlrd
import numpy as np

def calculate_s(file_path):
    sheet = xlrd.open_workbook(file_path).sheet_by_index(0)

    row_num = sheet.nrows-2

    square_sum = 0
    sum = 0
    for index in range(0, row_num):
        square_sum = square_sum + sheet.cell(index+1, 2).value ** 2
        sum = sum + sheet.cell(index+1, 2).value
        print square_sum
        print sum

    s = square_sum/sum**2

    return s