# Импортировать библиотеки pyplot и openpyxl

from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx') # Загрузить таблицу Excel из файла в переменную wb
sheet=wb['Data'] # Загрузить лист с именем "Data" в переменную sheet
sheet['A'][1:] # Получить содержимое колонки A в виде списка

def getvalue(x):
    return x.value
map(getvalue,sheet['A'][1:])# Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)

pyplot.plot(list_x, list_y,label="Метка")
pyplot.show()
