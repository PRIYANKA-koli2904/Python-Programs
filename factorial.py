#1.Write  a program to get factorial of a number using while loop.
# Taking input from the user
num = int(input("Enter a number: "))

# Initialize the result to 1
result = 1

# Use while loop to calculate factorial
while num > 1:
    result *= num
    num -= 1

# Output the result
print("Factorial is:", result)
