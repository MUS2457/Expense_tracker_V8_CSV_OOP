Expense Tracker CLI (Python)

A command-line Expense Tracker built with Python.
The program allows users to record daily expenses, analyze spending patterns, and search expenses by date. Data is stored in a readable CSV file for easy access and review.

Features

Add expenses with product name, category, and price

Automatic timestamp generation

Expense analysis:

Total and average spending

Category totals and averages

Most and least expensive products

Products above overall average

Categories above overall average

Highest and lowest spending categories

Search expenses by date (MM/DD/YYYY)

CSV data persistence (easy to open in Excel)

Technical Concepts & Skills Used

Object-Oriented Programming (OOP)

Class methods and instance methods

CSV file handling (read/write)

Data type conversion (string → float)

Nested dictionaries

Dictionary aggregation and grouping

Loop control (break, continue, flags like found)

Input validation

Modular project structure (separating logic, data handling, and tools)

Command-Line Interface (CLI) design

Project Structure

class_method → Expense class and calculations

data_handling → CSV loading and saving

input_data → User expense input

calculations → Analysis logic

tools → Search functionality

main.py → Program entry point and menu system

How to Run

Make sure Python 3 is installed.

Run:

python main.py


Choose from the menu:

1 → Analyse expenses

2 → Search expenses by date

3 → Exit

Data Storage

Expenses are saved in CSV format:

timestamp,product,category,price
02/19/2026, 14:14:01,Shampo,Cleaning,600.0
02/19/2026, 14:14:14,Beef,Meat,1390.0

Author

Personal project built in 3 days for real-life use and practical learning.
