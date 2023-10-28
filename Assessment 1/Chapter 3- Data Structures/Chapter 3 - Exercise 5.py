# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#same as Exercise 4
# People invited to dinner
people = ['Christian', 'Christ', 'tian']

# Print a message inviting each person in the list to dinner
for person in people:
    print(f"Hey {person}, would you like dinner?")

# Someone can't make it to dinner :(
unavailable_guest = 'Christ'
print(f"\nUnfortunately, {unavailable_guest} will not come.")

# Replace the unavailable guest with a new person
new_person = 'Crist na wlang h'
people[people.index(unavailable_guest)] = new_person

# Print a second set of invitation messages for the updated guest list
print("\nUpdated invitation list:")
for person in people:
    print(f"Hey {person}, would you like dinner?")

