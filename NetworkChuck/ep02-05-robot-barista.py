#robot barista

print("Welcome to our coffe shop.")
name = input("What is your name?\n")

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
    print("Hello " + name + ".")
menu = "Espresso, Lungo, Dopio, Quadruple dopio espresso with extra heartattack for free"
print("Here is our menu. \n" + menu)
order = input("What would you like?\n")

if order == "Lungo":
    price = 3.50
elif order == "Dopio":
    price = 4
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

quantity = int(input("How many coffees would you like?\n"))

total = (quantity * price)
print("That will be " + str(total) + "$.")

if order == "Quadruple dopio espresso with extra heartattack for free" and quantity == 1:
    print("We will have your " + str(quantity) + " " + order + " ready in a minute.\n\n\nAre you all right " + name + "? It looks like you are having heartattack. I am calling 911!")
elif order == "Quadruple dopio espresso with extra heartattack for free" and quantity >= 2:
    print("We will have your " + str(quantity) + " Quadruple dopio espressos with extra heartattack for free ready in a minute.\n\n\nAre you all right " + name + "? It looks like you are having heartattack. I am calling 911!")
elif order != "Quadruple dopio espresso with extra heartattack for free" and quantity == 1:
    print("We will have your " + str(quantity) + " " + order + " ready in a minute.")
elif order != "Quadruple dopio espresso with extra heartattack for free" and quantity >= 2:
    print ("We will have your " + str(quantity) + " " + order + "s ready in a minute.")

#if order == "Espresso":
#    print("That will be " + str(quantity * 3) + "$.")
#elif order == "Lungo":
#    print("That will be " + str(quantity * 3.50) + "$.")
#elif order == "Dopio":
#    print("That will be " + str(quantity * 4) + "$.")
#elif order == "Quadruple dopio espresso with extra heartattack for free":
#    print("That will be " + str(quantity * 4.50) + "$.")

def my_function(milk = "With" or milk = "Without"):
my_function = input('mi: ')
    print(milk)
    

