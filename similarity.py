import xlrd
import numpy as np

FILE_PATH = ''

def get_row_num():
    sheet = xlrd.open_workbook(FILE_PATH).sheet_by_index(0)
    data_row_num = sheet.nrows-1
    return data_row_num


def get_col_num():
    sheet = xlrd.open_workbook(FILE_PATH).sheet_by_index(0)
    data_col_num = sheet.ncols - 1
    return data_col_num


def get_all_vectors():
    file_path = FILE_PATH
    book = xlrd.open_workbook(file_path)
    sheet = book.sheet_by_index(0)

    data_row_num = get_row_num()
    data_col_num = get_col_num()

    a = np.zeros((data_row_num, data_col_num))

    for row_index in range(0, data_row_num):
        for col_index in range(0, data_col_num):
            a[row_index][col_index] = sheet.cell(row_index+1, col_index+1).value

    return a


def calculate_similarity():
    b = get_all_vectors()
    a = np.zeros((get_row_num(), get_col_num()))

    for index1 in range(0, get_row_num() - 1):
        for index2 in range(index1 + 1, get_row_num()):
            if sum(b[index1] ** 2) ** 0.5 * sum(b[index2] ** 2) ** 0.5 != 0:
                c = (np.dot(b[index1], b[index2])) / (np.linalg.norm(b[index1]) * np.linalg.norm(b[index2]))
                print c
                a[index1][index2] = c
            else:
                print 0.0
                a[index1][index2] = 0.0

    return a


def calculate_difference():
    b = get_all_vectors()
    a = np.zeros((get_row_num(), get_col_num()))

    for index1 in range(0, get_row_num() - 1):
        for index2 in range(index1 + 1, get_row_num()):
            if sum(b[index1] ** 2) ** 0.5 * sum(b[index2] ** 2) ** 0.5 != 0:
                c = 1 - (np.dot(b[index1], b[index2])) / (np.linalg.norm(b[index1]) * np.linalg.norm(b[index2]))
                print c
                a[index1][index2] = c
            else:
                print 1.0
                a[index1][index2] = 1.0

    return a
