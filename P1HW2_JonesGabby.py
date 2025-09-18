# Gabby Jones
# 9/18/2025
# P1HW2
# Program performs basic math on numbers that are entered

# Function to calculate and display travel expenses

print ("This program calculates and displays travel expenses")

# Get budget from user
budget = int(input ("Enter Budget: "))
print()
# Get travel destination from user
travel_destination = input ("Enter your travel destination: ")
print()
# Get estimated gas price from user
gas = int(input ("How much do you think you will spend on gas? "))
print()
# Get estimated hotel price from user
hotel = int(input ("Approximately, how much will you need for accommodation/hotel? "))
print()
# Get food price from user
food = int(input ("Last, how much do you need for food? "))
print()
# Calculate the remaining balance
remaining_balance = budget - gas - hotel - food

# Output results
print ("--------Travel Expenses--------")

print(f"Location: {travel_destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {hotel}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")