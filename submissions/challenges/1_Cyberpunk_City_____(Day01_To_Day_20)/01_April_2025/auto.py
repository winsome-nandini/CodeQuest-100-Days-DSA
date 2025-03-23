import os
from datetime import datetime, timedelta

# Set the start date
start_date = datetime(2025, 4, 1)

# Number of days
num_days = 100

# Define folder mappings for different day ranges
base_dirs = {
    range(1, 21): r"C:\Users\Dell\Desktop\CodeQuest\-CodeQuest-100-Days-DSA\submissions\challenges\1_Cyberpunk_City_____(Day01_To_Day_20)",
    range(21, 41): r"C:\Users\Dell\Desktop\CodeQuest\-CodeQuest-100-Days-DSA\submissions\challenges\2_Mysterious_Island____(Day21_To_Day_40)",
    range(41, 61): r"C:\Users\Dell\Desktop\CodeQuest\-CodeQuest-100-Days-DSA\submissions\challenges\3_Hackers_Heist_______(Day41_To_Day_60)",
    range(61, 81): r"C:\Users\Dell\Desktop\CodeQuest\-CodeQuest-100-Days-DSA\submissions\challenges\4_Magical_World____(Day61_To_Day_80)",
    range(81, 101): r"C:\Users\Dell\Desktop\CodeQuest\-CodeQuest-100-Days-DSA\submissions\challenges\5_Final_Showdown__(Day81_To_Day_100)"
}

# Loop to create folders for 100 days
for i in range(num_days):
    date = start_date + timedelta(days=i)
    day_number = i + 1  # Day count (1 to 100)
    
    # Determine the correct parent directory
    parent_dir = None
    for day_range, path in base_dirs.items():
        if day_number in day_range:
            parent_dir = path
            break
    
    if parent_dir:  # If a valid parent directory is found
        folder_name = date.strftime("%d_%B_%Y")  # Format: DD_Month_YYYY
        folder_path = os.path.join(parent_dir, folder_name)

        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

print("All folders created successfully!")
