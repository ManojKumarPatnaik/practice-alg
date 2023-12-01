def solution(A):
  """
  Determines the minimum number of relocations required to ensure the company never falls into debt.

  Args:
      A (list[int]): An array of revenues and expenses, where positive numbers represent revenues and negative numbers represent expenses.

  Returns:
      int: The minimum number of relocations required to avoid debt.
  """

  # Initialize the number of relocations to 0
  relocations = 0

  # Initialize the total sum to 0
  total = 0

  # Create an empty list to store the current batch of expenses
  batch = []

  # Iterate through the array of revenues and expenses
  for number in A:
    # Append the current number to the batch
    batch.append(number)

    # Update the total sum by adding the current number
    total += number

    # Check if the total sum is negative
    if total < 0:
      # Increment the number of relocations
      relocations += 1

      # Sort the batch of expenses in ascending order
      batch.sort()

      # Remove the smallest expense (negative number) from the batch
      smallest_expense = batch.pop(0)

      # Subtract the smallest expense from the total sum
      total -= smallest_expense

  # Return the total number of relocations
  return relocations

print(solution([10, -10, -1, -1, 10]))  # Output: 1
print(solution([-1, -1, -1, 1, 1, 1, 1]))  # Output: 3
print(solution([5, -2, -3, 1]))  # Output: 0