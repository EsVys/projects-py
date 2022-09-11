items_without_milk = {
    'espresso': 2.00,
    'lungo': 2.50,
    'dopio': 3.00,
    'cold brew': 2.50
}
items_without_milk_str = str(items_without_milk)

items_with_milk = {
    'latte': 4.00,
    'cappuccino': 3.50
}
items_with_milk_str = str(items_with_milk)

def add_milk(price_without_milk: float):
    milk = input('Do you wish to add oat milk?\n').lower()
    if milk == 'yes': 
        return price_without_milk + 0.25
    elif milk == 'no':
        return price_without_milk
    elif milk != 'yes' or milk != 'no':
        print('The value is not correct, please chose valid option.')
        return add_milk(milk)
    return price_without_milk

def get_order(name: str):
    #menu, order
    print('Here is our menu. \n' + items_without_milk_str + ', ' + items_with_milk_str + '.')
    order = input('What would you like?\n').lower()

    #price calculation
    if order in items_without_milk:
        price = add_milk(items_without_milk[order])
    elif order in items_with_milk:
        price = items_with_milk[order]
    else:
        print('Sorry, we do not have that here.')
        exit()
    quantity = int(input('How many coffees would you like?\n'))
    validate_input_quantity(quantity)
    total = float(price) * float(quantity)
    print('The price is $' + str(total) + '.')

def validate_input_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print('The value is not correct, only positive numbers are allowed.')
            return validate_input_quantity()
        return quantity
    except ValueError:
        print('The value is not correct, only numbers are allowed.')
        return validate_input_quantity()
        