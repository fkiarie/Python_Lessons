def calculate_interest_rate(period: int) -> float:
  """Calculates the interest rate based on the borrowing period.

  Args:
    period: The borrowing period in weeks.

  Returns:
    The interest rate.
  """

  return 0.12 if period > 2 else 0.07

def calculate_total_loan_amount(principal_amount: int, interest_rate: float) -> float:
  """Calculates the total loan amount, including interest.

  Args:
    principal_amount: The amount of money borrowed.
    interest_rate: The interest rate.

  Returns:
    The total loan amount, including interest.
  """

  loan_amount = principal_amount * interest_rate
  total = loan_amount + principal_amount
  return total

def main():
  """Calculates the total loan amount, including interest."""

  principal_amount = int(input("Enter the amount borrowed: "))
  period = int(input("Enter the borrowing period (in weeks): "))

  interest_rate = calculate_interest_rate(period)
  total_loan_amount = calculate_total_loan_amount(principal_amount, interest_rate)

  print(f"Total amount to pay after {period} weeks: {total_loan_amount}")

if __name__ == "__main__":
  main()
