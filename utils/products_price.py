def selling_price(
        cost_price: float,
        margin: float,
        sub_item_quantity = 1
    ):

    if(sub_item_quantity == None):
        sub_item_quantity = 1

    cost_price = cost_price/sub_item_quantity
    
    selling_price = round(cost_price * (1 + (margin/100)), 2)

    int_part = int(selling_price)
    dec_part = int((selling_price - int_part) * 100)

    if 0 <= dec_part <= 20:
        dec_part = 20
    elif 20 < dec_part <= 50:
        dec_part = 50
    else:
        dec_part = 99

    selling_price = float(f'{int_part}.{dec_part}')

    return selling_price
