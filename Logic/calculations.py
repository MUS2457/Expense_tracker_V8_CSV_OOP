from data.class_method import Expense

def most_least_price (expenses) :
    higher_product_price = float('-inf')
    higher_product_category = ''
    higher_product = ''
    lower_product_price = float('inf')
    lower_product_category = ''
    lower_product = ''

    if expenses :
        for expense in expenses :
            if expense.price > higher_product_price:
                higher_product_price = expense.price
                higher_product_category = expense.category
                higher_product = expense.product

            if expense.price < lower_product_price:
                lower_product_price = expense.price
                lower_product_category = expense.category
                lower_product = expense.product

        return (higher_product_price, higher_product_category, higher_product,
                lower_product_price, lower_product_category, lower_product
        )

    return None, None,None,None,None,None


def product_higher_than_average(expenses):

    total, average = Expense.total_expenses(expenses)
    bigger_average = {}

    if average is None :
        return None

    for expense in expenses :
        if expense.price > average :
            bigger_average[expense.product] = expense.price
    return bigger_average

def category_higher_than_average(expenses):

    total, average = Expense.total_expenses(expenses)
    category, average_per_category = Expense.total_expenses_category(expenses)

    bigger_average = {}

    if average is None :
        return None

    for category ,averages in average_per_category.items() :
        if averages > average :
            bigger_average[category] = averages

    return bigger_average

def max_min_spent_category (expenses):
    category, average = Expense.total_expenses_category(expenses)
    if category :
        highest = max(category, key= lambda x : category[x]["total"])
        lowest = min(category, key= lambda x : category[x]["total"])

        return (highest, lowest, category[highest]["total"],category[highest]["count"],
                category[lowest]["total"],category[lowest]["count"])

    return None, None, None, None
