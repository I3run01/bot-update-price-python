def selling_price(cost_price: float, margin: float):
    selling_price = cost_price*(1+ (margin/100))

    selling_price_decimal = str(selling_price)[-2]

    print(selling_price)
    print(selling_price_decimal)

selling_price(2.43, 40)