#Q.1) WAP to get the factorial of a number using a function
# Function to calculate factorial
# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input number from user
num = int(input("Enter a number to calculate its factorial: "))

# Output the factorial
print(f"The factorial of {num} is {factorial(num)}")
