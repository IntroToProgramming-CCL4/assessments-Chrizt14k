# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms
# to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.


# Create a dictionary called glossary to store programming words and their meanings
glossary = {
    'variable': 'A container for storing data values.',
    'list': 'An ordered, and changeable, collection of items.',
    'tuple': 'An ordered, and unchangeable, collection of elements.',
    'dictionary': 'A collection that allows us to store data in key-value pairs.',
    'function': 'A block of code that performs a specific task and can be reused whenever needed.',
    'class': 'A blueprint for creating objects that have certain attributes and methods.',
    'module': 'A file containing Python definitions and statements.',
    'string': 'A sequence of characters.',
    'integer': 'A whole number, positive or negative, without decimals.',
    'float': 'A number, positive or negative, containing one or more decimals.'
}

# Print each word and its meaning as neatly output.
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")

