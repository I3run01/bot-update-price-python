import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(script_dir)

sys.path.insert(1, parent_dir)

from utils.products_price import selling_price

class Product:
    def __init__(
            self,
            is_new: bool,
            ours_code: str, 
            c_ean: str,
            cost_price: float,
            ncm: str,
            commercial_name: str,
            margin: float,
            old_selling_price: float
        ):
        self._is_new = is_new
        self._ours_code = ours_code
        self._c_ean = c_ean
        self._cost_price = cost_price
        self._ncm = ncm
        self._commercial_name = commercial_name
        self._selling_cost = selling_price(cost_price, margin)
        self._old_selling_price = old_selling_price
    
    @property
    def ours_code(self):
        return self._ours_code

    @property
    def c_ean(self):
        return self._c_ean

    @property
    def cost_price(self):
        return self._cost_price

    @property
    def ncm(self):
        return self._ncm

    @property
    def commercial_name(self):
        return self._commercial_name

    @property
    def selling_cost(self):
        return self._selling_cost
    
    @property
    def old_selling_price(self):
        return self._old_selling_price
