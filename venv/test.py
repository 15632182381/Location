import xlrd as a


data = a.open_workbook_xls(r'C:/Users/hujl/Desktop/1.xlsx')
print (data.sheet_names())