from typing import Union, Literal
import pyperclip
import pyautogui
import time

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


def update_price(products: list, status: Union[Literal['increase'], Literal['any']]):
    pyautogui.PAUSE = 1.5

    open_gestor()

    pyautogui.click(200,650)
    pyautogui.click(200,360)

    for product in products:

        if(status == 'increase'):

            if(product.old_selling_price > product.new_selling_price and product.ours_code):
                continue

            if(product.ours_code):
                is_produc_exists_internally = True
            else: 
                is_produc_exists_internally = False

            #Confirming if product exists
            if(is_produc_exists_internally == False):
                pyautogui.press('esc')
                pyautogui.click(200,460)
                pyautogui.write(product.c_ean)
                pyautogui.press('Enter')

                pyperclip.copy('')

                pyautogui.doubleClick(50,310)

                pyautogui.hotkey('ctrl', 'c')

                text = pyperclip.paste().strip()

                if(len(text) < 2):
                    is_produc_exists_internally = False

                else:
                    is_produc_exists_internally = True

                pyautogui.press('Enter')

                pyautogui.press('esc')

                pyautogui.press('Tab')

                pyautogui.press('Enter')

                pyautogui.click(200,360)

            if(is_produc_exists_internally):
                product.ours_code = text

                update_product_price(product, status)

    

