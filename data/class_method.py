from datetime import datetime

class Expense:
    def __init__(self, product, category , price):
        self.product = product
        self.category = category
        self.price = price
        self.timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    @classmethod
    def total_expenses(cls, expenses):
        if not expenses:
            return None, None

        total = sum(exp.price for exp in expenses)
        average = round(total / len(expenses) ,1) if len(expenses) else None
        return total, average

    @classmethod
    def total_expenses_explicit(cls, expenses):
        if not expenses:
            return None, None           # Explicit version - for future reference / remind myself nostalgic way
        total = 0
        count = 0
        for exp in expenses:
            total += exp.price
            count += 1
        return total, round(total / len(expenses) ,1)

    @classmethod
    def total_expenses_category(cls, expenses):

        category = {}

        if not expenses:
            return {}, {}

        for exp in expenses:
            if exp.category not in category:
                category[exp.category] = {
                    "total": exp.price,
                    "count": 1
                }
            else:
                category[exp.category]["total"] += exp.price   #using nested data access to add value safely
                category[exp.category]["count"] += 1

        average_per_category = {}

        for cat, info in category.items():
            average = round(info["total"] / info["count"], 1)
            average_per_category[cat] = average

        return category, average_per_category


    def to_dictionary(self):
        return {"timestamp" : self.timestamp, "product": self.product, "category": self.category, "price": self.price}

    @classmethod
    def from_dictionary(cls, dictionary):
        expenses = {}
        class_exp = cls(dictionary["product"], dictionary["category"],dictionary["price"])
        expenses[dictionary["timestamp"]] = class_exp
        return expenses