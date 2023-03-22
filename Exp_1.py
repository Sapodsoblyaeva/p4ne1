from matplotlib import pyplot
from openpyxl import load_workbook

wb=load_workbook('Orders_all.xlsx')
sheet=wb['Total']
sheet['A'][7:18]

def getvalue(x):
    return x.value

list_of_customers = list(map(getvalue, sheet['A'][7:18]))
list_of_prices = list(map(getvalue, sheet['F'][7:18]))

pyplot.plot(list_of_customers, list_of_prices, label='total_2022')
pyplot.legend()
pyplot.show()