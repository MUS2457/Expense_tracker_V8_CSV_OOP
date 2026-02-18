from data.data_handling import load_csv

list_of_expenses = load_csv()

def search_expence():
    while True:
        searched_date = input(
            "Please enter the date you would like to search for in the format (DD-MM-YYYY), "
            "or type 'exit' to quit : "
        ).strip()

        if searched_date == 'exit':
            print("Exiting...")
            break

        if not searched_date:
            print("Please enter a valid date.")
            continue

        total_that_day = 0
        category = {}
        expenses_info = {}
        found = False

        if list_of_expenses:
            for expence in list_of_expenses:
                for timestamp, obj in expence.items():
                    if timestamp.startswith(searched_date):
                        found = True
                        total_that_day += obj.price

                        expenses_info[timestamp] = {"product": obj.product, "category": obj.category, "price": obj.price}

                        if obj.category in category:
                            category[obj.category] += obj.price
                        else:
                            category[obj.category] = obj.price

            if found:
                return {
                    "expenses" : expenses_info,
                    "total spent": total_that_day,
                    "total spent per category": category
                }
            else:
                print("No expenses found on that date.")
                return False
        else:
            print("No expenses available.")
            return found
