# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    

# List of people I would like to invite to dinner
people = ['Christian', 'Christ', 'tian']

# Print an invitation message for each person in the list
for person in people:
    print("Hey " + person + ", would you like to join me for dinner?")
    
# you can use + instead of the {} where it is sometimes hard to see the difference of [] and {}
# Someone can't make it to dinner
unavailable_guest = 'Christ'
print("\nUnfortunately, " + unavailable_guest + " can't make it to dinner.")

# Replace the unavailable guest with a new person
new_person = 'ian'
index_of_unavailable_guest = people.index(unavailable_guest)
people[index_of_unavailable_guest] = new_person

# Print a second set of invitation messages for the updated guest list
print("\nUpdated invitation list:")
for person in people:
    print("Hey " + person + ", would you like to join me for dinner?")
#Exercise 5 part

# New information: Only two guests can be invited
print("\nsorry I can only invite two people for dinner, my bad.")

# Remove guests from the list until only two names remain
while len(people) > 2:
    removed_guest = people.pop()
    print("Sorry, " + removed_guest + ", I can't invite you to dinner, I'm very sorry.")

# Print invitation messages for the two remaining guests
print("\nInvitation for the remaining guests:")
for person in people:
    print("Hey " + person + ", you're still invited to dinner, Please come.")

# Empty the list
del people[:]

print ("\n")
# Print the empty list to confirm
print("\nUpdated invitation list:", people)

