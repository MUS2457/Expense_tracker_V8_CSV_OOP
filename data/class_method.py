
class Expense:
    def __init__(self, name, category , price):
        self.name = name
        self.category = category
        self.price = price

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
            return {}
        for exp in expenses:
            if exp.category not in category:
                category[exp.category] = exp.price
            else:
                category[exp.category] += exp.price

        return category

