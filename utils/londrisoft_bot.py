from typing import Union, Literal
import pyperclip
import pyautogui
import time
from datetime import datetime

current_date = datetime.now()

current_day = current_date.day
current_month = current_date.month
current_year = current_date.year

pyautogui.PAUSE = 1.8

def open_gestor():

    #open the gestor
    pyautogui.press('winleft')
    pyautogui.write('gestor')
    pyautogui.press('enter')
    pyautogui.tripleClick(400, 340)
    pyautogui.hotkey('ctrl','c')

    copied_text = pyperclip.paste().strip()

    if(copied_text != 'mercadovizinhanca1762@gmail.com'):
        print(copied_text)
        raise ValueError("pyautogui crashed")
    
    pyautogui.click(400, 430)
    pyautogui.write('1515')
    pyautogui.press('enter')

def update_product_price(
        product: object,
        status: Union[Literal['increase'], Literal['any']]
):
    code_verifification = str(current_day) + str(current_month) + str(current_year)

    pyautogui.tripleClick(200, 200)

    pyautogui.write(product.ours_code)

    pyautogui.press('Enter')

    pyautogui.press('Enter')

    pyautogui.tripleClick(750, 650)

    if(status == 'any'):
        new_price = product.new_selling_price

        new_price_with_comma = new_price.replace(".", ",")

        pyautogui.write(new_price_with_comma)

        pyautogui.press('Enter')

    pyautogui.hotkey('ctrl', 'c')

    content_price_str = pyperclip.paste().strip().replace(",", ".")

    ls_price = float(content_price_str)

    if(
        ls_price >= product.new_selling_price and
        product.ours_code[0: len(code_verifification) != str(code_verifification)]
    ):
        product.new_selling_price = ls_price

        product.print_product = False

        print(product.nfe_name)

    else:
        new_price_str = str(product.new_selling_price)

        new_price = new_price_str.replace('.', ',')

        pyautogui.write(new_price)

        pyautogui.press('Enter')

    pyautogui.click(300, 100)

def has_product_in_LS(product):
    if(product.ours_code):
        return True
    
    if(product.ours_code == None and product.c_ean == None):
         raise ValueError(f"The Product {product.nfe_name} has no cEAN and Ours code")

    pyautogui.press('esc')
    pyautogui.click(200,460)
    pyautogui.write(product.c_ean)
    pyautogui.press('Enter')

    pyperclip.copy('')

    pyautogui.doubleClick(29,310)

    pyautogui.hotkey('ctrl', 'c')

    text = pyperclip.paste().strip()

    pyautogui.press('Enter')

    pyautogui.press('esc')

    pyautogui.press('Tab')

    pyautogui.press('Enter')

    pyautogui.click(200,360)

    if(len(text) > 30):
        return False

    product.ours_code = text

    return True


#TODO: verify
def create_product(product):

    attempts = 0
    while True:

        unique_code = str(current_day) + str(current_month) + str(current_year) + str(attempts)

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

        attempts = attempts + 1

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

def print_labels(our_codes: list):
    pyautogui.click(900,520)
    pyautogui.click(250,100)

    for our_code in our_codes:

        pyautogui.tripleClick(400,400)
        pyautogui.write(our_code)
        time.sleep(.5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.click(480,600)
        pyautogui.press('enter')
        pyautogui.click(260,60)

    pyautogui.press('esc')

    pyautogui.click(450, 30)

    pyautogui.click(450, 30)

def update_and_print_products(products: list, status: Union[Literal['increase'], Literal['any']]):
    
    open_gestor()

    pyautogui.click(200,650)
    pyautogui.click(200,360)

    for product in products:

        if(status == 'increase'):

            if(product.old_selling_price > product.new_selling_price and product.ours_code):
                continue

            has_product_internally = has_product_in_LS(product)
           
            if(has_product_internally):
                update_product_price(product, status)

            else:
                create_product(product)
        
        else: 
            has_product_internally = has_product_in_LS(product)
           
            if(has_product_internally):
                update_product_price(product, status)

            else:
                create_product(product)
                
    pyautogui.press('esc')

    pyautogui.press('esc')

    pyautogui.press('Enter')

    pyautogui.click(750, 27)

    pyautogui.click(750, 27)

    our_code_print_list = []
    for product in products:

        if(status == 'increase'):
            if(
                product.new_selling_price > product.old_selling_price 
                and product.print_product
            ):
                our_code_print_list.append(product.ours_code)
        
        else:
           our_code_print_list.append(product.ours_code) 

    print_labels(our_code_print_list)

def just_update_products(products: list, status: Union[Literal['increase'], Literal['any']]):

    open_gestor()

    pyautogui.click(200,650)
    pyautogui.click(200,360)

    for product in products:

        if(status == 'increase'):

            if(product.old_selling_price > product.new_selling_price and product.ours_code):
                continue

            has_product_internally = has_product_in_LS(product)
           
            if(has_product_internally):
                update_product_price(product, status)

            else:
                create_product(product)
        
        else: 
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
