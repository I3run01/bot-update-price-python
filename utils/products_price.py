def selling_price(
        cost_price: float,
        margin: float,
        selling_price: None or float = None
    ):

    if(selling_price):
        return selling_price

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
