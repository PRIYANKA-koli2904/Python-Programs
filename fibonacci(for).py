#Q.2)WAP to get factorial of a number
# Input from the user
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i  # Multiply the current number with factorial

# Output the result
print(f"The factorial of {num} is {factorial}")
