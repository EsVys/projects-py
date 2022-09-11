    #total price calculation, purchase completion
    #total = calculate_total(price, quantity)

    final_print(order, quantity)

    #when the customer returns, the system remembers them

    #repeat_order(order, name, total)

#def calculate_total(price: float, quantity: int) -> float:
    #total = (quantity * price)
    #print_total(total)
    #return total

#def print_total(total):
    #print('That will be $' + str(total) + '.')
        
def final_print(order, quantity):
    we_will = 'We will have your '
    ready = ' ready in a minute.'
    hot_warning = 'Be careful, this drink is hot.'
    #if order in items_without_milk[0:3] and quantity == 1:
        #print(we_will + order + ready + '\n' + hot_warning)
    #elif order in items_without_milk[0:3] and quantity >= 2:
        #print(we_will + str(quantity) + " " + order + 's' + ready + '\n' + hot_warning)
    #elif order == items_without_milk[3] and quantity == 1:
        #print(we_will + str(quantity) + " " + order + ready)
    # elif order == items_without_milk[3] and quantity >= 2:
        #print (we_will + str(quantity) + " " + order + 's' + ready)
    
    return order

def repeat_order(order, name, total):
    print('Hello, welcome back ' + proper_name + '!')
    repeat = input('Should I repeat your last order?\n').lower()
    if repeat == 'yes':
        confirmation = input('Your last order was: ' + order + '. Is it correct?').lower()
        if confirmation == 'yes':
            print_total(total)
    else:
        get_order(name)
