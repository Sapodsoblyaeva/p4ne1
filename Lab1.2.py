# Импортировать библиотеки pyplot и openpyxl

from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx') # Загрузить таблицу Excel из файла в переменную wb
sheet=wb['Data'] # Загрузить лист с именем "Data" в переменную sheet
sheet['A'][1:] # Получить содержимое колонки A в виде списка

def getvalue(x):
    return x.value
A = list(map(getvalue,sheet['A'][1:]))# Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
B = list(map(getvalue,sheet['C'][1:]))
C = list(map(getvalue,sheet['D'][1:]))
pyplot.plot(A, B, label="Метка")
pyplot.plot(A, C, label="Метка2")
pyplot.legend()
pyplot.show()
