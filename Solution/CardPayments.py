def solution(A, D):
  """Computes the final balance of a bank account at the end of the year 2020,
  given a list of all the transactions on the account during the year, and taking
  into account the card fee.

  Args:
    A: A list of N integers representing transaction amounts.
    D: A list of N strings representing transaction dates in YYYY-MM-DD format.

  Returns:
    The final balance of the account at the end of the year 2020.
  """

  # Create a dictionary to store the payments made in each month.
  monthlyPayments = {f"{i + 1:02d}": [] for i in range(12)}

  # Iterate over the transactions.
  for i in range(len(A)):
    # Get the month of the transaction.
    month = D[i].split("-")[1]

    # If there is no entry for the month in the dictionary, create one.
    if A[i] < 0:
      monthlyPayments[month].append(A[i])

  # Keep track of how many months had at least 3 card payments and a total
  # cost of at least 100.
  deductedFees = 0
  for month, payments in monthlyPayments.items():
    if len(payments) >= 3 and abs(sum(payments)) >= 100:
      deductedFees += 1

  # Compute the final balance of the account, taking into account the card fee.
  return sum(A) - 5 * (12 - deductedFees)

print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))  # Output: 230
print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))  # Output: 25
print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))  # Output: -164
print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))  # Output: 80
print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))  # Output: -115
