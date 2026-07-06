# import shutil
# from pathlib import Path

# TRACKED_EXTENSIONS = {
#     "Documents": [".pdf", ".docx", ".txt"],
#     "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
#     "Archives": [".zip", ".tar", ".rar"]
# }

# folders = ["Documents","Images","Archives","Unrecognized"]
# for folder in folders: 
#     new_folder = Path(f"Day05_Local_File_Organization/{folder}")
#     new_folder.mkdir(parents=True, exist_ok=True)
#     print(f"Folder '{new_folder}' is ready to use!")

# folder_path = Path("Day05_Local_File_Organization/Test_Folder")

# for file_path in folder_path.iterdir():
#         if file_path.is_file():
#             print(f"Processing: {file_path.name}")
#             print(file_path.suffix)
#             if file_path.suffix in  TRACKED_EXTENSIONS["Documents"]:
#                 destination_folder = Path("Day05_Local_File_Organization\Documents")
#                 shutil.move(file_path, destination_folder)
#                 print(f"Successfully moved {file_path.name}")
#             elif file_path.suffix in  TRACKED_EXTENSIONS["Images"]:
#                 destination_folder = Path("Day05_Local_File_Organization\Images")
#                 shutil.move(file_path, destination_folder)
#                 print(f"Successfully moved {file_path.name}")
#             elif file_path.suffix in  TRACKED_EXTENSIONS["Archives"]:
#                 destination_folder = Path("Day05_Local_File_Organization\Archives")
#                 shutil.move(file_path, destination_folder)
#                 print(f"Successfully moved {file_path.name}")
#             else:
#                 destination_folder = Path("Day05_Local_File_Organization/Unrecognized")
#                 shutil.move(file_path, destination_folder)
#                 print(f"Successfully moved {file_path.name}")
            
import shutil
from pathlib import Path

BASE_DIR = Path("Day05_Local_File_Organization")
TEST_FOLDER = BASE_DIR / "Test_Folder"

TRACKED_EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Archives": [".zip", ".tar", ".rar"]
}

all_folders = list(TRACKED_EXTENSIONS.keys()) + ["Unrecognized"]
for folder in all_folders: 
    (BASE_DIR / folder).mkdir(parents=True, exist_ok=True)

if not TEST_FOLDER.exists():
    print(f"⚠️ Test folder '{TEST_FOLDER}' does not exist! Populate it first.")
else:
    for file_path in TEST_FOLDER.iterdir():
        if file_path.is_file():
            # Lowercase the suffix to catch extension mismatches like '.PDF'
            file_ext = file_path.suffix.lower()
            # Initialize default destination category
            matched_folder = "Unrecognized"
            for category, extensions in TRACKED_EXTENSIONS.items():
                if file_ext in extensions:
                    matched_folder = category
                    break  # Stop checking other categories once a match is hit

            destination_folder = BASE_DIR / matched_folder
            shutil.move(str(file_path), str(destination_folder / file_path.name))
            print(f"📦 Moved: '{file_path.name}' ➡️ [{matched_folder}]")