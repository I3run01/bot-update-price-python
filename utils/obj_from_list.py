def find_product_by_ean(product_list, c_ean):
    for product in product_list:
        if product.c_ean == c_ean:
            return product
    return None
