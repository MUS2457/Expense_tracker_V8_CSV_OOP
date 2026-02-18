import csv
import os

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
