import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(script_dir)

sys.path.insert(1, parent_dir)

from utils.products_price import selling_price

class Product:
    def __init__(
            self,
            c_prod: str,
            ours_code: str or None, 
            c_ean: str or None,
            cost_price: float,
            ncm: str,
            cest: str or None,
            commercial_name: str | None,
            nfe_name: str,
            margin: float,
            old_selling_price: float,
        ):
        self._c_prod = c_prod
        self._ours_code = ours_code
        self._c_ean = c_ean
        self._cost_price = cost_price
        self._ncm = ncm
        self._cest = cest
        self._commercial_name = commercial_name
        self._nfe_name = nfe_name
        self._margin = margin
        self._new_selling_price = selling_price(cost_price, margin)
        self._old_selling_price = old_selling_price
        self._sub_item_quantity = None
        self._print_product = True
    
    @property
    def c_prod(self):
        return self._c_prod

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
    def cest(self):
        return self._cest

    @property
    def commercial_name(self):
        return self._commercial_name
    
    @property
    def nfe_name(self):
        return self._nfe_name
    
    @property
    def margin(self):
        return self._margin

    @property
    def new_selling_price(self):
        return self._new_selling_price
    
    @property
    def old_selling_price(self):
        return self._old_selling_price
    
    @property
    def sub_item_quantity(self):
        return self._sub_item_quantity
    
    @property
    def print_product(self):
        return self._print_product
    
    @margin.setter
    def margin(self, value: float):
        self._margin = value
        self._new_selling_price = selling_price(self._cost_price, self._margin)

    @ours_code.setter
    def ours_code(self, value: str):
        self._ours_code = value

    @new_selling_price.setter
    def new_selling_price(self, value: str):
        self._new_selling_price = value

        # self.margin = ((self.new_selling_price/self.cost_price) - 1)*100 

    @c_ean.setter
    def c_ean(self, value: str):
        self._c_ean = value

    @sub_item_quantity.setter
    def sub_item_quantity(self, value: str):
        self._sub_item_quantity = value

        self._cost_price = self._cost_price/value

        self._new_selling_price = selling_price(
            self._cost_price,
            self._margin
        )
    
    @print_product.setter
    def print_product(self, value: bool):
        self._print_product = value
        

