#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# Make a list called sandwich_orders and fill it with the names of various sandwiches.
sandwich_orders = ['tuna','turkey','cuban','veggie','ham']

# Make an empty list called finished_sandwiches.
finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for each order.
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Print a message listing each sandwich that was made.
print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
