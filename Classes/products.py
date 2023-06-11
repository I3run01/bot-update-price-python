class Products:
    def __init__(
            self,
            isNew: bool,
            ours_code: str, 
            cEAN: str,
            cost_price: float,
            ncm: str,
            commercial_name: str,
            selling_cost: float,
            old_selling_price: float
        ):
        self.__isNew = isNew
        self.__ours_code = ours_code
        self.__cEAN = cEAN
        self.__cost_price = cost_price
        self.__ncm = ncm
        self.__commercial_name = commercial_name
        self.__selling_cost = selling_cost
        self.__old_selling_price = old_selling_price

    def get_isNew(self):
        return self.__isNew
    
    def get_ours_code(self):
        return self.__ours_code

    def get_cEAN(self):
        return self.__cEAN

    def get_cost_price(self):
        return self.__cost_price

    def get_ncm(self):
        return self.__ncm

    def get_commercial_name(self):
        return self.__commercial_name

    def get_selling_cost(self):
        return self.__selling_cost
    
    def get_old_selling_price(self):
        return self.__old_selling_price
