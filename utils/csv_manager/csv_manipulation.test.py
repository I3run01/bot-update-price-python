import csv_manipulation as csv

path = 'database/NS & FG INDUSTRIA E COMERCIO DE PRODUTOS ALIMENTICIOS LTDA.csv'

cProd = 'f3570'

procucts_data = csv.get_row_by_cProd(
    file_path=path, 
    cProd=cProd)

print(procucts_data)
