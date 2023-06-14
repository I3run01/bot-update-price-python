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

    for product in product:
        print(product)

        if(product.old_selling_price > product.new_selling_price):
            continue

    pyautogui.tripleClick(420,200)
