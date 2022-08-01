#robot barista

from html.entities import name2codepoint

# To Do:
# fix function greet when no name
# solution for milk input
# crete a dictionary with price for each item
# with the next order the robot will ask if the customer wants to repeat the next order using the variables from functions


items_without_milk = ['Espresso', 'Lungo', 'Dopio', 'Quadruple dopio espresso with extra heartattack for free']
items_without_milk_str = ', '.join(items_without_milk)
items_with_milk = ['Latte', 'Cappuccino']
items_with_milk_str = ', '.join(items_with_milk)

def greet(greeting, name = 'Darling'):
    print("Hello! Welcome to our coffe shop.")
    name = input("What is your name?\n")
    age = int(input('What is your age, ' + name + '?\n'))
    if age <= 16:
        print('We are sorry, ' + name + ' we do not anything for you here.')
        exit()
    else:
        pass

    return name
    
def final_print(order):
    we_will = "We will have your "
    ready = " ready in a minute."
    all_right = "\n\n\nAre you all right, " + name + "? It looks like you are having heartattack. I am calling 911!"
    if order == items_without_milk[3] and quantity == 1:
        print(we_will + str(quantity) + " " + order + ready + all_right)
    elif order == items_without_milk[3] and quantity >= 2:
        print(we_will + str(quantity) + " Quadruple dopio espressos with extra heartattack for free" + ready + all_right)
    elif order != items_without_milk[3] and quantity == 1:
        print(we_will + str(quantity) + " " + order + ready)
    elif order != items_without_milk[3] and quantity >= 2:
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
    elif name != "Ben" or "Pat":
        pass

    return name

greeting = 'Hi!'
name = greet(greeting)
    
evil_status(name)

print("Here is our menu. \n" + items_without_milk_str + ', ' + items_with_milk_str + '.')
order = input("What would you like?\n")


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

total = (quantity * price)

print("That will be " + str(total) + "$.")

# pri najblizsej objednavke sa zakaznika spyta, co bola jeho posledna objednavka a ci ju chce zopakovat