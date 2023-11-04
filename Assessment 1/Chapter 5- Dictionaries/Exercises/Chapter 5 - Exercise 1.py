# Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.


# Create a dictionary to store information about a person.
person = {
    'first_name': 'Christian',
    'last_name': 'Altar',
    'age': 30,
    'city': 'New york'
}
# Print each information stored in the dictionary.
print("First name: " + person['first_name'])  # Access the value of the 'first_name' key and print it
print("Last name: " + person['last_name'])  # Access the value of the 'last_name' key and print it
print("Age: " + str(person['age']))  # Access the value of the 'age' key, convert it to a string, and print it
print("City: " + person['city'])  # Access the value of the 'city' key and print it
