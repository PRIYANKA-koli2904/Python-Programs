#4).Create a while loop to print the Fibonacci series up to n terms.
# Taking input from the user
n = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1
count = 0

# Use a while loop to generate the Fibonacci series
while count < n:
    print(a, end=" ")  # Print the current Fibonacci number
    a, b = b, a + b    # Update a and b to the next Fibonacci numbers
    count += 1          # Increment the count

