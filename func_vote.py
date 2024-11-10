#3) Function to check voting eligibility
def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

# Input age from user
age = int(input("Enter your age: "))

# Output whether the person can vote or not
if can_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
