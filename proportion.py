import xlrd
import numpy as np


def calculate_proportion(file_path, diff_matrix):
    sheet = xlrd.open_workbook(file_path).sheet_by_index(0)

    row_num = sheet.nrows-2

    d_matrix = np.zeros((row_num, row_num))
    for index1 in range(0, row_num-1):
        for index2 in range(index1+1, row_num):
            d = diff_matrix[index1][index2]*sheet.cell(index1+1, 3).value*sheet.cell(index2+1, 3).value
            d_matrix[index1][index2] = d
            print d

    return d_matrix