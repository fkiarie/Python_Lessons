def add_expenses(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expenses["amount"]}, Category {expenses["category"]}')
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

