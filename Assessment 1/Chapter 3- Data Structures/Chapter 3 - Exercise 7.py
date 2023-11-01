# Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# List of places to visit
places_to_visit = ['Japan', 'Korea', 'Switzerland', 'Mt everest', 'afterlife']

# Print the list in its original order
print("Original order:", places_to_visit)

# Print the list in alphabetical order using sorted()
print("Alphabetical order:", sorted(places_to_visit))

# Print the list again to show it's still in its original order
print("Original order:", places_to_visit)

# Print the list in reverse alphabetical order using sorted()
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Print the list again to show it's still in its original order
print("Original order:", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()

# Print the list to show the changed order
print("Reversed order:", places_to_visit)
