# This script is an expense tracker that allows users to add, list, and filter expenses.

# expenses: A list to store all the expenses. Each expense is a dictionary with 'amount' and 'category' keys.
# add_expense(expenses, amount, category): A function to add a new expense to the expenses list.
# print_expenses(expenses): A function to print all the expenses in the expenses list.
# total_expenses(expenses): A function to calculate the total amount of all expenses.
# filter_expenses_by_category(expenses, category): A function to filter expenses based on a given category.
# main(): The main function that controls the flow of the program.

def add_expense(expenses, amount, category):
    # Add a new expense to the expenses list
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    # Print all the expenses in the expenses list
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    # Calculate the total amount of all expenses
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    # Filter expenses based on a given category
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    global expenses
    expenses =[]
    while True: 
        # Display the main menu and get user's choice
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            # Add a new expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            # Show total expenses
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            # Filter expenses by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()