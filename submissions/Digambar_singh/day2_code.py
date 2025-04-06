import time
print("Hello, Cyberpunk City!")
name = input("What is your name? >> ")
hour = time.localtime().tm_hour
if 5 <= hour < 12:
    greet = "Good morning"
elif 12 <= hour < 18:
    greet = "Good afternoon"
elif 18 <= hour < 22:
    greet = "Good evening"
else:
    greeting = "Good night"
print(f"{greet}, {name}! Welcome to the adventure!")