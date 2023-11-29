def calculate_discount(price,discount_percent):
    if discount_percent>=20:
        discount_price = discount_percent/100*price
    else:
        discount_price = 0
    return f'your final price is {price-discount_price}'

price = int(input('Please, Input your price '))
discount_percent = int(input('Please, Input the discount '))
print(calculate_discount(price,discount_percent))
