# Day 3 : Escape the Cyber Hackers!

# Takeing user input
name = input("Enter your name: ")

# Generating secret code
secret_code = name[::-1].upper()

# Displaying results
print(f"Original Name: {name}")
print(f"Secret Code: {secret_code}")