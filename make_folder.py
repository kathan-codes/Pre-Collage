import shutil
from pathlib import Path

source_folder = Path("Day")

if not source_folder.exists():
    print(f"Error: The template folder '{source_folder}' does not exist!")
    print("Please create it first, then re-run this script.")
else:
    for i in range(1, 31):
        # :02d forces the number to have 2 digits (e.g., 1 becomes 01, 10 stays 10)
        new_folder_name = f"Day{i:02d}_"
        destination_folder = Path(new_folder_name)
        
        # 4. Copy the folder if it doesn't already exist
        if not destination_folder.exists():
            shutil.copytree(source_folder, destination_folder)
            print(f"Created: {new_folder_name}")
        else:
            print(f"Skipped: {new_folder_name} (Already exists)")

    print("\nAll 30 folders are ready!")
