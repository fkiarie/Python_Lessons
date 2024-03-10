def add_expenses(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expenses["amount"]}, Category {expenses["category"]}')
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
