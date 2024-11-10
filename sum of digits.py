#3)Write a while loop to calculate the sum of digits of a given number.
# Taking input from the user
num = int(input("Enter a number: "))

# Initialize the sum to 0
sum_of_digits = 0

# Use while loop to calculate the sum of digits
while num > 0:
    sum_of_digits += num % 10  # Add the last digit to sum
    num //= 10  # Remove the last digit

# Output the result
print("Sum of digits:", sum_of_digits)
