from typing import Union, Literal
import pyperclip
import pyautogui
import time
from datetime import datetime
import random
import pyperclip

current_date = datetime.now()

current_day = current_date.day
current_month = current_date.month
current_year = current_date.year

code_verifification = str(current_day) + str(current_month) + str(current_year)

random_num_list = []

pyautogui.PAUSE = 0.5

def from_main_menu_to_product_registration():
    time.sleep(1.5)

    pyautogui.click(200,650)

    time.sleep(1.5)

    pyautogui.click(200,360)

    time.sleep(5)

def from_product_registration_to_main_menu():
    pyautogui.press('esc')

    time.sleep(1.5)

    pyautogui.click(500,660)

    time.sleep(1.5)

    pyautogui.press('Enter')

    time.sleep(1.5)

    pyautogui.click(100, 330)

    time.sleep(2)

def is_product_created_today(our_code):
    return our_code[0: len(str(code_verifification))] == str(code_verifification)

def unique_randoms():
    while True:
        random_number = random.randint(0, 99)
        
        if random_number not in random_num_list:
            random_num_list.append(random_number)
            return random_number

def open_gestor():
    pyautogui.PAUSE = 0.5
    gestor_path = r'C:\londrisoft\Gestor_Prime\gestor.exe'
    email = 'mercadovizinhanca1762@gmail.com'
    password = '1515'

    #open the gestor
    pyautogui.hotkey('winleft','r')
    pyautogui.write(gestor_path)
    pyautogui.press('Enter')

    time.sleep(2)

    pyautogui.hotkey('winleft', 'tab')

    time.sleep(0.5)

    pyautogui.press('left')

    pyautogui.press('Enter')

    time.sleep(1.5)

    pyautogui.tripleClick(400, 350)

    pyautogui.hotkey('ctrl','c')

    copied_text = pyperclip.paste().strip()

    if copied_text != email:
        raise ValueError(f"Error: the app crashed")

    pyautogui.write(email)

    pyautogui.press('tab')

    pyautogui.write(password)

    pyautogui.press('Enter')

    time.sleep(7)

def update_product_price(
        product: object
    ):

    pyautogui.tripleClick(200, 200)

    pyautogui.write(product.ours_code)

    pyautogui.press('Enter')

    pyautogui.press('Enter')

    pyautogui.tripleClick(750, 650)

    pyautogui.hotkey('ctrl', 'c')

    content_price_str = pyperclip.paste().strip().replace(",", ".")

    ls_price = float(content_price_str)

    isProductCreatedToday = is_product_created_today(product.ours_code)

    if(ls_price >= product.min_new_selling_price and ls_price <= product.max_new_selling_price):
        product.new_selling_price = ls_price
        product.print_product = False

    else:
        new_price_str = str(product.new_selling_price)

        new_price = new_price_str.replace('.', ',')

        pyautogui.write(new_price)

        pyautogui.press('Enter')

        print(10*'-')
        print(product.ours_code)
        print(10*'-')

        if(isProductCreatedToday):
            product.print_product = True

    pyautogui.click(300, 100)

def has_product_in_LS(product):
    if(product.ours_code):
        return True
    
    if(product.ours_code == None and product.c_ean == None):
         raise ValueError(f"The Product {product.nfe_name} has no cEAN and Ours code")
    pyautogui.tripleClick(200, 200)

    pyautogui.write('GENERICO')

    pyautogui.press('Enter')

    pyperclip.copy('')

    pyautogui.tripleClick(600, 200)
    pyautogui.write(product.c_ean)
    pyautogui.press('Enter')

    time.sleep(1.5)

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('Enter')
    copied_text = pyperclip.paste().strip()

    if(len(copied_text) < 15):
        return False
    
    pyautogui.tripleClick(100, 200)

    pyautogui.hotkey('ctrl', 'x')
    product_code = pyperclip.paste().strip()
    pyautogui.hotkey('ctrl', 'z')

    product.ours_code = product_code

    return True

def create_product(product):
    pyautogui.PAUSE = 0.5
    while True:

        unique_code = str(current_day) + str(current_month) + str(current_year)[-2:]

        unique_code += str(unique_randoms())

        pyautogui.click(250, 100)

        pyautogui.write(unique_code)

        pyautogui.press('Enter')

        pyautogui.tripleClick(750, 650)

        pyperclip.copy('')

        pyautogui.hotkey('ctrl', 'c')

        text = pyperclip.paste().strip()

        if(len(text) > 10):
            pyautogui.press('Enter')

        else:
            product.ours_code = unique_code
            break

    pyautogui.click(400, 200)

    pyautogui.write(product.c_ean)

    pyautogui.press('Enter')

    pyautogui.tripleClick(400, 230)

    if(product.commercial_name):
        pyperclip.copy(product.commercial_name)
    
    else:
        pyperclip.copy(product.nfe_name)

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.press('Enter')

    pyautogui.press('right')

    pyautogui.press('Enter')

    pyautogui.click(400, 662)

    pyautogui.moveTo(400, 690)

    time.sleep(1)

    pyautogui.click()

    pyautogui.tripleClick(750, 650)

    new_price = product.new_selling_price

    new_price_str = str(new_price).replace('.',',')

    pyautogui.write(new_price_str)

    pyautogui.press('Enter')

    pyautogui.click(200, 150)

    #tributes
    pyautogui.click(80, 235)

    pyautogui.write('040')

    pyautogui.doubleClick(130, 410)

    pyautogui.write('07')

    pyautogui.doubleClick(600, 410)

    pyautogui.write('07')

    pyautogui.doubleClick(130, 570)

    pyautogui.write(product.ncm)

    pyautogui.press('Enter')

    pyautogui.press('Enter')

    pyautogui.press('esc')

    pyautogui.press('Enter')

    pyautogui.press('Enter')

    if(product.cest):
        pyautogui.write(product.cest)

    pyautogui.click(140,150)

    pyautogui.click(300, 100)

    print(10*'-')
    print(product.ours_code)
    print(10*'-')

def print_labels(our_codes: list):

    pyautogui.click(900,520)

    time.sleep(1.5)

    pyautogui.click(250,100)

    for our_code in our_codes:

        pyautogui.tripleClick(400,400)
        pyautogui.write(our_code)
        time.sleep(.5)
        pyautogui.press('enter')
        pyautogui.press('enter')

        for c in range(0, 2):
            pyautogui.click(600,550)

            pyautogui.click(600,580)

        pyautogui.press('tab')

        pyautogui.press('Enter')

        time.sleep(7)

        pyautogui.press('Enter')

        for c in range(0, 6):
            pyautogui.press('Up')

        pyautogui.press('Enter')

    pyautogui.press('esc')

    pyautogui.click(450, 30)

    pyautogui.click(450, 30)

def update_and_print_products(products: list):

    open_gestor()

    from_main_menu_to_product_registration()

    for product in products:

        has_product_internally = has_product_in_LS(product)
        
        if(has_product_internally):
            update_product_price(product)

        else:
            create_product(product)
                
    from_product_registration_to_main_menu()

    our_code_print_list = []

    for product in products:
        if(product.print_product):
            our_code_print_list.append(product.ours_code)

    print_labels(our_codes=our_code_print_list)
    
def just_update_products(products: list, status: Union[Literal['increase'], Literal['any']]):

    open_gestor()

    pyautogui.click(200,650)
    pyautogui.click(200,360)

    for product in products:
        if(
            status == 'increase' and 
            product.old_selling_price >= product.new_selling_price and 
            product.ours_code and
            is_product_created_today(product.ours_code) == False
        ):    
            product.print_product = False
            continue

        has_product_internally = has_product_in_LS(product)
        
        if(has_product_internally):
            update_product_price(product, status)

        else:
            create_product(product)
                
def just_print_products(products: list, status: Union[Literal['increase'], Literal['any']]):

    open_gestor()

    our_code_print_list = []
    for product in products:

        if(status == 'increase'):
            if(product.new_selling_price > product.old_selling_price):
                our_code_print_list.append(product.ours_code)
        
        else:
           our_code_print_list.append(product.ours_code) 

    print_labels(our_code_print_list)
