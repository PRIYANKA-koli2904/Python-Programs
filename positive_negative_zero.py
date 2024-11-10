#check whether the number is positive, negative or zero.
# Get user input
number = float(input("Enter a number: "))  # Convert input to a float

# Check if the number is greater than zero
if number > 0:
    print("The number is positive.")
# Check if the number is less than zero
elif number < 0:
    print("The number is negative.")
# If neither, the number must be zero
else:
    print("The number is zero.")
