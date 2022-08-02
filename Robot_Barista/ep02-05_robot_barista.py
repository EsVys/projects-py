# To Do:
# solution for milk input (dictionary)
# create a dictionary with price for each item
# with the next order the robot will ask if the customer wants to repeat the next order using the variables from functions
# if the customer does not wish to repeat order start with new order

# price // espresso 2, lungo 2.50, dopio 3, quad 5.50. Mlieko + 0.25. Latte 4, Cappuccino 3.50. Idealne to spravit ako dictionary, kedy bude mat espresso priradenu cenu 2.
# Dictionary
# items = {
#    'espresso': 2.00,
#
#}
# price = items[order]


items_without_milk = ['Espresso', 'Lungo', 'Dopio', 'Cold brew']
items_without_milk_str = ', '.join(items_without_milk)
items_with_milk = ['Latte', 'Cappuccino']
items_with_milk.append('Flat white')
items_with_milk_str = ', '.join(items_with_milk)

def greet(greeting):
    print("Hello! Welcome to our coffe shop.")

    name = input("What is your name?\n")
    if not bool(name):
        name = 'Darling'

    age = int(input('What is your age, ' + name + '?\n'))
    if age <= 16:
        print('We are sorry, ' + name + ' we do not anything for you here.')
        exit()

    return name
    
def final_print(order, quantity):
    we_will = "We will have your "
    ready = " ready in a minute."
    hot_warning = " Be careful, this drink is hot."
    if order in items_without_milk[0:3] and quantity == 1:
        print(we_will + order + ready + '\n' + hot_warning)
    elif order in items_without_milk[0:3] and quantity >= 2:
        print(we_will + str(quantity) + " " + order + "s" + ready + '\n' + hot_warning)
    elif order == items_without_milk[3] and quantity == 1:
        print(we_will + str(quantity) + " " + order + ready)
    elif order == items_without_milk[3] and quantity >= 2:
        print (we_will + str(quantity) + " " + order + "s" + ready)
    
    return order

def evil_status(name):
    if (name == "Ben") or (name == "Pat"):
        evilst = input("Are you evil?\n")
        if evilst == "No":
            print("Oh, come on in!")
        elif evilst == "Yes" and 4 <= int(input("How many good deeds have you done today?\n")):
            print("All right, you can have a coffee.")
        else: 
            print("No coffee for you!.")
            exit()

# int je podmnozina float. prvy riadok vrati float z float a int.
def calculate_total(price: float, quantity: int) -> float:
    total = (quantity * price)
    print_total(total)
    return total

def print_total(total):
    print("That will be $" + str(total) + ".")

def repeat_order(order, name, total):
    print('Hello, welcome back ' + name + '!')
    repeat = input('Should I repeat your last order?\n')
    if repeat == 'Yes':
        confirmation = input('Your last order was: ' + order + '. Is it correct?')
        if confirmation == 'Yes':
            print_total(total)
    else:
        get_order(name)

def main():
    #greeting, age check
    greeting = 'Hi!'
    name = greet(greeting)

    #name, evil status check   
    evil_status(name)
    get_order(name)

def get_order(name: str):
    #menu, order
    print("Here is our menu. \n" + items_without_milk_str + ', ' + items_with_milk_str + '.')
    order = input("What would you like?\n")

    #price calculation
    if order == "Lungo":
        price = 3.50
    elif order == "Dopio":
        price = 4
    elif order == "Latte":
        price = 5
    elif order == "Quadruple dopio espresso with extra heartattack for free":
        price = 4.50
    elif order == "Espresso":
        milk = input("With oat milk? Or without?\n")
        if milk == "With":
            price = 3.25
        elif milk == "Without":
            price = 3
        else:
            print('Please chose valid option.')
            input()
    else:
        print("Sorry, we do not have that here.")
        price = 0
        exit()

    quantity = int(input("How many coffees would you like?\n"))

    #total price calculation, purchase completion
    total = calculate_total(price, quantity)

    final_print(order, quantity)

    #when the customer returns the system remembers them

    repeat_order(order, name, total)

if __name__ == "__main__":
    main()