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

def update_price(products: list, status: Union[Literal['increase'], Literal['any']]):
    pyautogui.PAUSE = 1.5

    open_gestor()

    pyautogui.click(200,650)
    pyautogui.click(200,360)

    for product in products:
        print(product)

        if(status == 'increase'):

            if(product.old_selling_price > product.new_selling_price):
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

                print(is_produc_exists_internally)

                if(is_produc_exists_internally):
                    print('')

            

