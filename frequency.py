import xlrd
import numpy as np

def calculate_s(file_path):
    sheet = xlrd.open_workbook(file_path).sheet_by_index(0)

    row_num = sheet.nrows-2

    frequency_vector = np.zeros(row_num)

    for index in range(0, row_num-1):
        frequency_vector[index] = sheet.cell(index+1, 2).value

    s = np.dot(frequency_vector, frequency_vector)/np.linalg.norm(frequency_vector)

    return s