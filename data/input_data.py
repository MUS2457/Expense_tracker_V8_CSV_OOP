from data.class_method import Expense

def get_product() :
    while True :
        product = input("Enter product name ,'done' to finish and 'exit' to quit : ").strip()

        if product in ('done', 'exit') :
            return product.lower()
        elif not product or any(char.isdigit() for char in product) :
            print("Invalid product name")
            continue
        else:
            return product.capitalize()

def get_category(product) :
    while True :
        category = input(f"Enter category of {product} : ").strip()

        if not category or any(char.isdigit() for char in category) :
            print("Invalid category name")
            continue
        return category.capitalize()

def get_price(product, category) :
    while True:
        try:
            price = float(input(f"Enter the price of {product} ({category}): "))
            if price < 0:
                print("Price cannot be negative")
                continue
            return price
        except ValueError:
            print("Invalid price")

def get_expense() :
    expenses = []
    while True :
        product = get_product()

        if product == 'exit' :
            print("Exit the program")
            break
        elif product == 'done' :
            break

        category = get_category(product)
        price = get_price(product, category)

        grocery = Expense(product, category, price)

        expenses.append(grocery)

    return expenses
