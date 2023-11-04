# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python'):
    print(f"I make a {size} shirt with the message of '{message}' printed on it.")

# Make a large shirt and a medium shirt with the default message.
make_shirt()
make_shirt('medium')

# Make a shirt of any size with a different message.
make_shirt('small', 'Python is fun!')

