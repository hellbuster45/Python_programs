# Input for the first time in hours and minutes
hours1 = int(input("Enter the hours for the first time: "))
minutes1 = int(input("Enter the minutes for the first time: "))

# Input for the second time in hours and minutes
hours2 = int(input("Enter the hours for the second time: "))
minutes2 = int(input("Enter the minutes for the second time: "))

# Calculate total hours and minutes
total_hours = hours1 + hours2
total_minutes = minutes1 + minutes2

# Adjust total_hours and total_minutes if minutes exceed 60
if total_minutes >= 60:
    total_hours += total_minutes // 60
    total_minutes = total_minutes % 60

print(f"Total time: {total_hours} hours and {total_minutes} minutes")