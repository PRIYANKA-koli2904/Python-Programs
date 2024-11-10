#2)Write a while loop that counts the number of digits in a given number
# Taking input from the user
num = int(input("Enter a number: "))

# Initialize the digit count to 0
count = 0

# Use while loop to count the digits
while num > 0:
    num //= 10  # Remove the last digit
    count += 1  # Increment the digit count

# Output the result
print("Number of digits:", count)
