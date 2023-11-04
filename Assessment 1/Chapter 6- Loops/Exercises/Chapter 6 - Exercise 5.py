# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# Make a list called sandwich_orders and fill it with the names of various sandwiches.
sandwich_orders = ['tuna', 'turkey','cuban', 'pastrami', 'veggie', 'ham', 'pastrami', 'pastrami']

# Make an empty list called finished_sandwiches.
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami.
print("Sorry, we have run out of pastrami.")

# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders and print a message for each order.
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Print a message listing each sandwich that was made.
print("\nsandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())


