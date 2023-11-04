#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
while True:
    topping = input("Please enter a pizza topping (enter 'quit' to exit):")
    if topping == 'quit':
        break  # break is used to exit a loop prematurely
    else:
        print(f"I'll add {topping} to your pizza.")
