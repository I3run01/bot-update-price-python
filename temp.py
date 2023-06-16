from utils.londrisoft_bot import update_price
from Classes.Product import Product

products_list = [
    Product(
        is_new=True,
        ours_code=None,
        c_ean="7896336006624",
        cost_price=1,
        ncm="abcd",
        commercial_name="Poçoca",
        nfe_name="Poçoca",
        margin=50,
        old_selling_price=0.0,
    ),
    # Product(
    #     is_new=False,
    #     ours_code="2345",
    #     c_ean="2345678901234",
    #     cost_price=150.0,
    #     ncm="efgh",
    #     commercial_name="Product Commercial Name 2",
    #     nfe_name="Product NFe Name 2",
    #     margin=30,
    #     old_selling_price=200.0,
    # ),
    # Product(
    #     is_new=True,
    #     ours_code="3456",
    #     c_ean="3456789012345",
    #     cost_price=200.0,
    #     ncm="ijkl",
    #     commercial_name="Product Commercial Name 3",
    #     nfe_name="Product NFe Name 3",
    #     margin=25,
    #     old_selling_price=250.0,
    # )

]

update_price(products_list, 'increase')