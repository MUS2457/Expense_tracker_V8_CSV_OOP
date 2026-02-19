from data.data_handling import load_csv

list_of_expenses = load_csv()

def search_expence():
    while True:
        searched_date = input(
            "Please enter the date you would like to search for in the format (MM/DD/YYYY), "
            "or type 'exit' to quit : "
        ).strip()

        if searched_date == 'exit':
            return "exit"

        if not searched_date:
            print("Please enter a valid date.")
            continue

        total_that_day = 0
        category = {}
        found = False
        info = {}

        if list_of_expenses:
            for expence in list_of_expenses:
                for timestamp, obj in expence.items():
                    if timestamp.startswith(searched_date):
                        found = True
                        total_that_day += obj.price
                        info[timestamp] = obj
                        if obj.category in category:
                            category[obj.category] += obj.price
                        else:
                            category[obj.category] = obj.price

            if found:
                return {
                    "expenses": info,
                    "total": total_that_day,
                    "categories": category
                }
            else:
                print("No expenses found on that date.")
                return False
        else:
            print("No expenses available.")
            return "no_expenses"
