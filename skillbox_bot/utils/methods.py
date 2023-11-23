def serialize_data(product):
    title = product['title']
    quantity = product['quantity']
    price = product['price']
    return f'Название: {title}, количество: {quantity}, цена: {price}'

# async def get_custom_sort():