def calculate_emi(principal, annual_interest_rate, tenure_years,
                  payments_per_year):
  """
  Calculate the EMI for a loan based on the reducing balance method.

  Args:
  principal (float): The principal amount of the loan.
  annual_interest_rate (float): The annual interest rate (percentage).
  tenure_years (int): The tenure of the loan in years.
  payments_per_year (int): The number of payments per year (1 for annually, 2 for semi-annually, 4 for quarterly, 12 for monthly).

  Returns:
  float: The EMI amount.
  """
  # Convert annual interest rate to rate per payment period and to a fraction
  period_interest_rate = annual_interest_rate / (payments_per_year * 100)
  # Convert tenure in years to total number of payments
  total_payments = tenure_years * payments_per_year

  # EMI formula for reducing balance method
  emi = (principal * period_interest_rate * (1 + period_interest_rate)**total_payments) / \
        ((1 + period_interest_rate)**total_payments - 1)

  return emi


def loan_schedule(principal, annual_interest_rate, tenure_years,
                  payments_per_year):
  """
  Generate the loan repayment schedule.

  Args:
  principal (float): The principal amount of the loan.
  annual_interest_rate (float): The annual interest rate (percentage).
  tenure_years (int): The tenure of the loan in years.
  payments_per_year (int): The number of payments per year (1 for annually, 2 for semi-annually, 4 for quarterly, 12 for monthly).

  Returns:
  list of tuples: A list where each tuple contains (payment_period, principal_paid, interest_paid, total_payment, remaining_balance).
  """
  period_interest_rate = annual_interest_rate / (payments_per_year * 100)
  total_payments = tenure_years * payments_per_year
  emi = calculate_emi(principal, annual_interest_rate, tenure_years,
                      payments_per_year)

  schedule = []
  remaining_balance = principal

  for period in range(1, total_payments + 1):
    interest_paid = remaining_balance * period_interest_rate
    principal_paid = emi - interest_paid
    remaining_balance -= principal_paid
    total_payment = principal_paid + interest_paid
    schedule.append((period, round(principal_paid, 2), round(interest_paid, 2),
                     round(total_payment, 2), round(remaining_balance, 2)))

  return schedule


def main():
  principal_amount = float(input("Enter the loan amount (principal): "))
  annual_interest_rate = float(
      input("Enter the annual interest rate (in %): "))
  tenure_years = int(input("Enter the loan tenure (in years): "))

  payment_mode = input(
      "Enter the mode of payment (monthly, quarterly, semi-annually, annually): "
  ).strip().lower()

  if payment_mode == 'monthly':
    payments_per_year = 12
  elif payment_mode == 'quarterly':
    payments_per_year = 4
  elif payment_mode == 'semi-annually':
    payments_per_year = 2
  elif payment_mode == 'annually':
    payments_per_year = 1
  else:
    print("Invalid payment mode selected. Defaulting to monthly.")
    payments_per_year = 12

  emi = calculate_emi(principal_amount, annual_interest_rate, tenure_years,
                      payments_per_year)
  schedule = loan_schedule(principal_amount, annual_interest_rate,
                           tenure_years, payments_per_year)

  print(f"Payment Period EMI: {emi:.2f}")
  print("\nLoan Repayment Schedule:")
  print(
      "Period | Principal Paid | Interest Paid | Total Payment | Remaining Balance"
  )
  for period, principal_paid, interest_paid, total_payment, remaining_balance in schedule:
    print(
        f"{period:>6} | {principal_paid:>14.2f} | {interest_paid:>13.2f} | {total_payment:>13.2f} | {remaining_balance:>17.2f}"
    )


if __name__ == "__main__":
  main()
