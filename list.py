#3)WAP to traverse a list of item and find particular item is present in the list or not
# Define a list of items
items = ['apple', 'banana', 'cherry', 'grape', 'orange']

# Input the item to search for
search_item = input("Enter the item to search: ")

# Traverse through the list to find the item
found = False  # Flag to track if item is found

for item in items:
    if item == search_item:
        found = True
        break  # Exit the loop if the item is found

# Check if the item was found
if found:
    print(f"{search_item} is present in the list.")
else:
    print(f"{search_item} is not present in the list.")
