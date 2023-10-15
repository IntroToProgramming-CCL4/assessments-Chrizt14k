# Import the datetime module
import datetime

#Get the current date and time and stores it in the variable current_datetime
current_datetime = datetime.datetime.now()

# Format the current date and time as a string  # (strftime) tool for formatting dates and times
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

# Print the current date and time
print("Current date and time:", formatted_datetime)
