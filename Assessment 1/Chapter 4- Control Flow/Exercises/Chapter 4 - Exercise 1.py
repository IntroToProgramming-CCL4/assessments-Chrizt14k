# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color ='green'

# if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
if alien_color == 'green':
    print("Wow, you just earned 5 points.")

# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
# Passes the test:
alien_color = 'green'
if alien_color == 'green':
    print("Wow, you just earned 5 points.")

# It failed the test and will not have an output
alien_color = 'red'
if alien_color == 'green':
    print("Wow, you just earned 5 points.")

