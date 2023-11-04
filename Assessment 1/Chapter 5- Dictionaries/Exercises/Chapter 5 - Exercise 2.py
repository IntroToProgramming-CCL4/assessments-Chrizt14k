#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.    

# Create a dictionary called glossary to store programming words and their meanings
# Get the meanings from research
glossary = {
 'variable': 'A container for storing data values',
 'list': 'An ordered, and changeable, collection of items',
 'tuple': 'An ordered, and unchangeable, collection of items',
 'dictionary': 'A collection that allows us to store data in key-value pairs',
'function': 'A block of code that performs a specific task and can be reused whenever needed'
}

# Print each word and its meaning as neatly output.
for word, meaning in glossary.items():
    print(word.title() + ":")
    print(meaning + "\n")



