import csv_manipulation as csv

path = '../../database/NS & FG INDUSTRIA E COMERCIO DE PRODUTOS ALIMENTICIOS LTDA.csv'

cProd = 'f3570'

procucts_data = csv.get_row_by_cProd(
    file_path=path, 
    cProd=cProd)

print(f'test 01:')
print(procucts_data)

product_from_eEAN = csv.get_row_by_cEAN(
    file_path = path,
    cEAN='f7898298160802'
)

print(f'test 02: ')
print(product_from_eEAN)

