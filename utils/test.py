import londrisoft_bot
import pyautogui

class Product:
    def __init__(self, ours_code, nfe_name, c_ean):
        self.ours_code = ours_code
        self.nfe_name = nfe_name
        self.c_ean = c_ean

product = Product(None, 'any', '78963360064')

pyautogui.PAUSE = 1.8

londrisoft_bot.open_gestor()

pyautogui.click(200,650)
pyautogui.click(200,360)

resp = londrisoft_bot.has_product_in_LS_v2(product)

print(resp)