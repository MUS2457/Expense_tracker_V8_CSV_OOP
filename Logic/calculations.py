from data import class_method, input_data
from data.class_method import Expense


def most_least_category_price (expenses) :
    categories = Expense.total_expenses_category(expenses)
    if categories :
        most_category = max(categories, key=categories.get)
        least_category = min(categories, key=categories.get)
        return (most_category, least_category,
                categories[most_category], categories[least_category]
                )
    else :
        return None, None,None,None

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