# Day 5: Local File Organization 🧹📁

## 📌 Project Overview
A system automation utility script that scans a designated local directory, automatically sorts misarranged files into dedicated sub-folders based on their extensions (e.g., documents, images, text files), and purges empty directories to keep the workspace clean.

## 🎯 Learning Objectives
* Master reading and navigating local file system directories.
* Learn safe file handling techniques (moving, copying, and sorting data).
* Understand how to cleanly manipulate system paths across different operating systems.

## 🛠️ Core Libraries Used
* `os` - For low-level operating system interactions and directory checking.
* `shutil` - For high-level file operations like moving and copying.
* `pathlib` - For modern, object-oriented file path manipulation.

## 🚀 How To Run
1. Navigate to this directory.
2. Run the script directly (it uses Python's built-in libraries, so no external `pip` installations are required for this day):
   ```bash
   python main.py