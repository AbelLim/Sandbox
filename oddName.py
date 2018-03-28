"""Ask user for name and print every second letter."""

# Ask user for name.
user_name = str(input("Please enter your name: "))
print(user_name)

# Check if user's name is blank.
while len(user_name.strip()) == 0:
    user_name = str(input("Please enter your name: "))
    print(user_name)
