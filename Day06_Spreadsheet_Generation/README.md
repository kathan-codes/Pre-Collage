# Day 6: Spreadsheet Generation 📊

## 📌 Project Overview
A data compiler script that processes a raw text file log of random financial costs, parses the information, and structures it into a cleanly formatted Excel spreadsheet complete with automatically calculated total columns.

## 🎯 Learning Objectives
* Learn how to programmatically write multidimensional arrays into tabular formats.
* Understand the structure of Excel files (workbooks, sheets, cells).
* Inject live, dynamic Excel cell formulas (`SUM`, etc.) using Python scripts.

## 🛠️ Core Libraries Used
* `csv` - For parsing baseline tabular or comma-separated raw logs.
* `openpyxl` - For building, formatting, and calculating formulas inside native `.xlsx` files.

## 🚀 How To Run
1. Navigate to this directory.
2. Install dependencies:
   ```bash
   pip install openpyxl