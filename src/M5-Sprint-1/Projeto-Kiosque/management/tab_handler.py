from menu import products


def calculate_tab(menu: list[dict]):
    subtotal = 0

    for consumed in menu:
        for product in products:
            if product['_id'] == consumed['_id']:
                subtotal += product['price'] * consumed['amount']

    return {'subtotal': f'${round(subtotal, 2)}'}
