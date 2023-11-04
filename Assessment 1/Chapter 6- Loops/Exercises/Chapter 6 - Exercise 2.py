# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

# Write a loop in which you ask users their age and then tell them the cost of their movie ticket.
while True:
    age = input("Please enter your age (enter 'quit' to exit): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("ticket is free.")
    elif age <= 12:
        print("The ticket costs $10.")
    else:
        print("The ticket costs $15.")
