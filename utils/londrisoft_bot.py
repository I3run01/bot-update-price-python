from typing import Union, Literal
import pyperclip
import pyautogui
import time
from datetime import datetime

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
    pyautogui.tripleClick(450, 200)

    pyautogui.write(product.c_ean)

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

    if(ls_price > product.new_selling_price):
        product.new_selling_price = ls_price

        print(product.new_selling_price)

    else:
        new_price_str = str(product.new_selling_price)

        new_price = new_price_str.replace('.', ',')

        pyautogui.write(new_price)

        pyautogui.press('Enter')

    pyautogui.click(300, 100)

def has_product_in_LS(product):
    if(product.ours_code):
        return True

    pyautogui.press('esc')
    pyautogui.click(200,460)
    pyautogui.write(product.c_ean)
    pyautogui.press('Enter')

    pyperclip.copy('')

    pyautogui.doubleClick(50,310)

    pyautogui.hotkey('ctrl', 'c')

    text = pyperclip.paste().strip()

    pyautogui.press('Enter')

    pyautogui.press('esc')

    pyautogui.press('Tab')

    pyautogui.press('Enter')

    pyautogui.click(200,360)

    if(len(text) < 1 or len(text) > 30):
        return False

    product.ours_code = text

    return True

def create_product(product):
    while True:
        current_date = datetime.now()

        attempts = 0

        current_day = current_date.day
        current_month = current_date.month
        current_year = current_date.year

        unique_code = str(current_day) + str(current_month) + str(current_year) + str(attempts)

        pyautogui.click(250, 100)

        pyautogui.write(unique_code)

        pyautogui.press('Enter')

        pyautogui.tripleClick(750, 650)

        pyperclip.copy('')

        pyautogui.hotkey('ctrl', 'c')

        text = pyperclip.paste().strip()

        if(len(text) > 10):
            attempts = attempts + 1

            pyautogui.press('Enter')

        else:
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
    
    pyautogui.write(product.cest)

    pyautogui.click(140,150)

    pyautogui.click(300, 100)

def update_price(products: list, status: Union[Literal['increase'], Literal['any']]):
    pyautogui.PAUSE = 1.5

    open_gestor()

    pyautogui.click(200,650)
    pyautogui.click(200,360)

    # for product in products:

    #     if(status == 'increase'):

    #         if(product.old_selling_price > product.new_selling_price and product.ours_code):
    #             continue

    #         has_product_internally = has_product_in_LS(product)
           
    #         if(has_product_internally):
    #             update_product_price(product, status)

    #         else:
    #             create_product(product)
                
    pyautogui.press('esc')

    pyautogui.press('esc')

    pyautogui.press('Enter')

    pyautogui.click(750, 27)
    
