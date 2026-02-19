from data import class_method, data_handling, input_data
from Logic import calculations, tools
from data.class_method import Expense


def analyse_expenses():
    expenses = input_data.get_expense()

    total, average = Expense.total_expenses(expenses)
    categories, category_average = Expense.total_expenses_category(expenses)

    (
        highest_product_price,
        highest_product_category,
        highest_product,
        lowest_product_price,
        lowest_product_category,
        lowest_product,
    ) = calculations.most_least_price(expenses)

    products_above_average = calculations.product_higher_than_average(expenses)
    categories_above_average = calculations.category_higher_than_average(expenses)

    (
        highest_category,
        lowest_category,
        highest_category_total,
        highest_category_count,
        lowest_category_total,
        lowest_category_count,
    ) = calculations.max_min_spent_category(expenses)

    print("=== Expense Analysis Results ===\n")

    print(f"Total expense amount: {total}")
    print(f"Average expense amount: {average}\n")

    print("Category Totals:")
    for category, info in categories.items():
        print(
            f"- {category}: Total = {info['total']}, "
            f"Number of items = {info['count']}"
        )

    print("\nCategory Averages:")
    for category, avg in category_average.items():
        print(f"- {category}: Average = {avg}")

    print(
        f"\nMost expensive product: {highest_product} "
        f"(Category: {highest_product_category}, Price: {highest_product_price})"
    )

    print(
        f"Least expensive product: {lowest_product} "
        f"(Category: {lowest_product_category}, Price: {lowest_product_price})"
    )

    if products_above_average:
        print("\nProducts priced above overall average:")
        for product, price in products_above_average.items():
            print(f"- {product}: {price}")

    if categories_above_average:
        print("\nCategories with average above overall average:")
        for category, avg in categories_above_average.items():
            print(f"- {category}: {avg}")

    print(
        f"\nCategory with highest total spending: {highest_category} "
        f"(Total: {highest_category_total}, Items: {highest_category_count})"
    )

    print(
        f"Category with lowest total spending: {lowest_category} "
        f"(Total: {lowest_category_total}, Items: {lowest_category_count})"
    )

    data_handling.save_csv(expenses)
    print("\nData saved successfully.")


def menu():
    print("\n=== Expense Tracker Menu ===")
    print("1. Analyse expenses")
    print("2. Search expenses by date")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            analyse_expenses()

        elif choice == "2":
             results = tools.search_expence()
             if results == "exit":
                 print("Goodbye!,returning to main menu.")
                 continue
             elif results is None:
                 print("No results found.")
                 continue
             elif results == "no_expenses" :
                 print("Try to use the main program to add expenses first, and run it again.")
                 continue
             else:
                 if results :
                     print("Expenses info")
                     print(results["expenses"])
                     print(f"Total expenses amount: {results['total']}")
                     print("\nCategory Totals:")
                     for category, info in results["categories"].items():
                        print(f"- {category}: Total = {info}")
                 else :
                     continue

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()


