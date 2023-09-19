from menu import products
from collections import Counter


def get_product_by_id(id: int) -> dict:
    if type(id) is not int:
        raise TypeError("product id must be an int")

    for index, dictionary in enumerate(products):
        if dictionary["_id"] == id:
            return products[index]

    return {}


def get_products_by_type(product_type: str) -> list[dict]:
    if type(product_type) is not str:
        raise TypeError("product type must be a str")

    list = [dictionary for index, dictionary in enumerate(
        products) if dictionary["type"] == product_type]

    return list


def add_product(menu: list[dict], **kwargs):
    new_id = 1

    if len(menu) > 0:
        last_id = [product["_id"] for product in menu]
        last_id.sort()
        new_id = last_id[-1] + 1

    kwargs["_id"] = new_id
    menu.append(kwargs)

    return kwargs


def menu_report():
    average_price = 0

    for product in products:
        average_price += product["price"]
    average_price = round(average_price / len(products), 2)

    most_common_type = Counter(product["type"] for product in products)

    return f"Products Count: {len(products)} - Average Price: ${average_price} - Most Common Type: {list(most_common_type)[0]}"


def add_product_extra(menu: list[dict], *args, **kwargs):
    id = 1
    if len(menu) > 0:
        index_list = [product["_id"] for product in menu]
        index_list.sort()
        id = index_list[-1] + 1

    new_product = dict(
        [
            (key, kwargs[f"{key}"])
            for key in kwargs
            for req_key in args
            if key == req_key
        ]
    )

    for req_key in sorted(args):
        try:
            new_product[f"{req_key}"]
        except KeyError:
            raise KeyError(f"field {req_key} is required") from None

    new_product["_id"] = id

    menu.append(new_product)

    return new_product
