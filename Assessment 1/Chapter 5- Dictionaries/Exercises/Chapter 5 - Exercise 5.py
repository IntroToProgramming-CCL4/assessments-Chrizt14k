# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet

# Create dictionaries where each dictionary represents a different pet
pet1 = {'animal':'dog','owner':'Christian'}
pet2 = {'animal':'cat','owner':'Tian'}
pet3 = {'animal':'lion','owner':'ian'}

# Store these dictionaries in a list called pets.
pets = [pet1, pet2, pet3]

# Loop through list and print 
for pet in pets:
    print(f"The {pet['animal']} is owned by {pet['owner']}.")

