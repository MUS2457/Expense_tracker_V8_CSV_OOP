import csv
import os
from data.class_method import Expense

def save_csv(expenses, filename="expense_tracker_v8.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=['timestamp', 'product', 'category', 'price']
        )

        if not file_exists:
            writer.writeheader()

        # write all expense objects since its list of obj so we should access each of them
        writer.writerows(exp.to_dictionary() for exp in expenses)

def load_csv(filename="expense_tracker_v8.csv"):
    expenses = []
    if not os.path.isfile(filename):
        return {}

    with open(filename, mode='r', newline='', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            exp = Expense.from_dictionary(row)  #exp is already a dic with key timestamp
            expenses.append(exp)
    return expenses   # so this return list of dic

