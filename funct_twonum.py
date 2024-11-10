#2) Function to find the maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Output the maximum number
print(f"The maximum of {num1} and {num2} is {find_max(num1, num2)}")
