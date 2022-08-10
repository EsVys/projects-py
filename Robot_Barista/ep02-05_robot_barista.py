# To Do:
# finish def get_order
# fix when no name print 'Darling'
# fix input name and proper_name
# solution for milk input (dictionary)
# with the next order the robot will ask if the customer wants to repeat the next order using the variables from functions
# if the customer does not wish to repeat order start with new order

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



def greet(name, greeting):
    print('Hello! Welcome to our coffe shop.')

    name = input('What is your name?\n')
    proper_name = {}
    proper_name[name.lower()] = name
    if not bool(name):
        name = 'Darling'

    greeting = 'Hi!'
    # name = greet(greeting)

    return(name, greeting)

def age_validation(age):
    age = int(input('What is your age, ' + proper_names[name] + '?\n'))
    validate_input()
    if age <= 16:
        print('We are sorry, ' + proper_name[name] + ' we do not anything for you here.')
        exit()

    return(age)

def validate_input():
    age = input('What is your age?\n')
    while age is not int:
        print('The value is not correct, only numbers are allowed.')
        if age is int:
            return(age)
        break

    validate_input()

def evil_status():
    name = greet(greeting)
    if (name == 'ben') or (name == 'pat'):
        evilst = input('Are you evil?\n').lower()
        if evilst == 'no':
            print('Oh, come on in!')
        elif evilst == 'yes' and 4 <= int(input('How many good deeds have you done today?\n')):
            print('All right, you can have a coffee.')
        else: 
            print('No coffee for you!.')
            exit()

def get_order(name: str):
    #menu, order
    print('Here is our menu. \n' + items_without_milk_str + ', ' + items_with_milk_str + '.')
    order = input('What would you like?\n').lower()

    #price calculation
    if order in items_without_milk:
        price = items_without_milk[order]
    elif order in items_with_milk:
        price = items_with_milk[order]
    else:
        print('Sorry, we do not have that here.')
        exit()
    quantity = int(input('How many coffees would you like?\n'))
    total = float(price) * float(quantity)
    print('The price is $' + str(total) + '.')


    #total price calculation, purchase completion
    #total = calculate_total(price, quantity)

    final_print(order, quantity)

    #when the customer returns, the system remembers them

    repeat_order(order, name, total)

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
    if order in items_without_milk[0:3] and quantity == 1:
        print(we_will + order + ready + '\n' + hot_warning)
    elif order in items_without_milk[0:3] and quantity >= 2:
        print(we_will + str(quantity) + " " + order + 's' + ready + '\n' + hot_warning)
    elif order == items_without_milk[3] and quantity == 1:
        print(we_will + str(quantity) + " " + order + ready)
    elif order == items_without_milk[3] and quantity >= 2:
        print (we_will + str(quantity) + " " + order + 's' + ready)
    
    return order

def repeat_order(order, name, total):
    print('Hello, welcome back ' + proper_name[name] + '!')
    repeat = input('Should I repeat your last order?\n').lower()
    if repeat == 'yes':
        confirmation = input('Your last order was: ' + order + '. Is it correct?').lower()
        if confirmation == 'yes':
            print_total(total)
    else:
        get_order(name)

def main():
    greeting = 'Hi!'
    name = greet(greeting)
    greet(greeting)
    age_validation(age)
    evil_status()
    get_order(name: str)
    calculate_total(price: float, quantity: int) -> float:
    print_total(total)
    final_print(order, quantity)
    repeat_order(order, name, total)
    



if __name__ == "__main__":
    main()