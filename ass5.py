def greet():
    print("Hello! Welcome to PizzaBot.")
    print("I will help you place your pizza order.")

def get_name():
    print("May I have your name, please?")
    name = input()
    print("Hi {}, nice to meet you!".format(name))
    return name

def choose_pizza():
    print("Here's our menu:")
    print("1. Margherita - ₹150")
    print("2. Pepperoni - ₹200")
    print("3. Veggie Delight - ₹180")
    print("4. Cheese Burst - ₹220")
    print("Please enter the number of the pizza you'd like to order:")
    
    while True:
        choice = input()
        if choice == '1':
            return "Margherita", 150
        elif choice == '2':
            return "Pepperoni", 200
        elif choice == '3':
            return "Veggie Delight", 180
        elif choice == '4':
            return "Cheese Burst", 220
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

def get_quantity():
    print("How many pizzas would you like to order?")
    while True:
        try:
            quantity = int(input())
            if quantity > 0:
                return quantity
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_address():
    print("Please enter your delivery address:")
    address = input()
    return address

def confirm_order(name, pizza, quantity, address, price):
    total = price * quantity
    print("\nHere is your order summary:")
    print("Name: {}".format(name))
    print("Pizza: {}".format(pizza))
    print("Quantity: {}".format(quantity))
    print("Price per Pizza: ₹{}".format(price))
    print("Total Amount: ₹{}".format(total))
    print("Delivery Address: {}".format(address))
    print("Thank you for your order! Your pizza will arrive shortly. 🍕")

def end_chat():
    print("It was a pleasure taking your order.")
    print("Goodbye and have a delicious day!")

# Run the chatbot
greet()
name = get_name()
pizza, price = choose_pizza()
quantity = get_quantity()
address = get_address()
confirm_order(name, pizza, quantity, address, price)
end_chat()
