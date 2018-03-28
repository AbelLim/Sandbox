"""Ask user for name and print every second letter."""

# Ask user for name.
user_name = str(input("Please enter your name: "))
print(user_name)

# Check if user_name is blank.
while len(user_name.strip()) == 0:
    user_name = str(input("Please enter your name: "))
    print(user_name)

# Print every character in user_name
for char in user_name:
    print(char)
