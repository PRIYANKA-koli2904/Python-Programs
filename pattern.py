#1)Print patterns
# Number of rows for the pattern
n = 4

# Loop through each row
for i in range(1, n + 1):
    # Print the left triangle with stars
    for j in range(1, i + 1):
        print("*", end=" ")
    
    # Print spaces between the two triangles
    print("   ", end="")  # Adjust space for proper formatting

    # Print the middle triangle with increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print spaces between the two triangles
    print("   ", end="")  # Adjust space for proper formatting

    # Print the right triangle with constant numbers (i repeated)
    for j in range(1, i + 1):
        print(i, end=" ")

    # Move to the next line after each row
    print()
