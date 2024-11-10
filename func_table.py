#4) Function to print the multiplication table of a number
def multiplication_table(number):
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{number} x {i} = {number * i}")

# Input number from user
num = int(input("Enter a number: "))

# Output the multiplication table
multiplication_table(num)
