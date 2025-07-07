import os
import utils.csv_manager.csv_manipulation as csv_manipulation
import utils.bot.londrisoft_bot as bot

cEAN_list = []
ours_code_list = []
database_path = './database'

csv_files = [os.path.join(database_path, file) for file in os.listdir(database_path) if file.endswith('.csv')]

while True:
    new_cEAN = input('Input cEAN or press Enter to continue: ')
    if new_cEAN == '':
        break
    cEAN_list.append(new_cEAN)

for cEAN in cEAN_list:

    for file in csv_files:
        try:
            product = csv_manipulation.get_row_by_cEAN(
                file_path=file,
                cEAN=f'f{cEAN}'
            )

            try:
                ours_code = product['ours_code'].unique()[0]

            except Exception:
                ours_code = product['ours_code']

            ours_code_list.append(ours_code[1:])

            break
        except Exception:
            continue

while True:
    retry = str(input('press ENTER to print: '))
    try:
        bot.open_gestor()
        bot.print_labels(
            ours_code_list
        )

    except Exception:
        'Error, try again'
