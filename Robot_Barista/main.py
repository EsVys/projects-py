# To Do:
# repeat order:
# with the next order the robot will ask if the customer wants to repeat the next order using the variables from functions
# if the customer does not wish to repeat order start with new order

import bouncer
import barista
import greet

def main():
    greeting = 'Hello!'
    name = greet.greet(greeting)
    age = bouncer.validate_input_age(name)
    #order = barista.get_order(name)
    #quantity = barista.get_order(name)                             
    bouncer.evil_status(name)
    barista.get_order(name)
    # barista.final_print(order, quantity)


if __name__ == "__main__":
    main()                                                  