# Set the price of each USB stick
usb_price = 6

# Set the girl's budget
budget = 50

# Calculate the number of USB sticks she can buy
num_usb = budget // usb_price

# Calculate the remaining money she will have
remaining_money = budget % usb_price

# Display the number of USB sticks she can buy
print("The girl can buy", num_usb, "USB sticks.")

# Display the amount of money she will have left
print("She will have", remaining_money, "left.")
