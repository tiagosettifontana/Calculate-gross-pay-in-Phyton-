# Prompt the user for hours and rate
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

# Convert the string inputs to float numbers
h = float(hrs)
r = float(rate)

# Calculate the gross pay
pay = h * r

# Print the result
print("Pay:", pay)