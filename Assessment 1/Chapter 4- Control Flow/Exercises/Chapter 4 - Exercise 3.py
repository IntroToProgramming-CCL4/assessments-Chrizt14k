#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, making sure each message is printed for the appropriate color alien.


# Add a variable called alien_color and assign it a value of green, yellow, or red.
alien_color = 'green'

# If it is green print a message that the player just earned points.
# Green = 5 points
# yellow = 10 points
# red = 15 points
if alien_color == 'green':
    print("Congrats, you just earned 5 points.")
elif alien_color == 'yellow':
    print("Congrats, you just earned 10 points.")
else:
    print("Congrats, you just earned 15 points.")


# Alien is green = 5
if alien_color == 'green':
    print("Congrats, you just earned 5 points.")
elif alien_color == 'yellow':
    print("Congrats, you just earned 10 points.")
else:
    print("Congrats, you just earned 15 points.")


# Alien is yellow = 10
alien_color = 'yellow'
if alien_color == 'green':
    print("Congrats, you just earned 5 points.")
elif alien_color == 'yellow':
    print("Congrats, you just earned 10 points.")
else:
    print("Congrats, you just earned 15 points.")


# Alien is red = 15
alien_color = 'red'
if alien_color == 'green':
    print("Congrats, you just earned 5 points.")
elif alien_color == 'yellow':
    print("Congrats, you just earned 10 points.")
else:
    print("Congrats, you just earned 15 points.")

