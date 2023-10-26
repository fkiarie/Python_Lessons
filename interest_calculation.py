interest_rate = 0
amt = input("Enter the amount borrowed: ")
principal_amt = int(amt)
period = input("Enter the borrowing period (in weeks): ")
period = int(period)

if period > 2:
    interest_rate = 0.12
else:
    interest_rate = 0.07

loan_amount = interest_rate * principal_amt
total = loan_amount + principal_amt

print(f"Total amount to pay after {period} weeks: {total}")
