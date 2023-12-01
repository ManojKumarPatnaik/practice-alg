def solution(R, V):
  """
  Returns the minimum initial account balances for banks A and B in order to complete the transfers.

  Args:
    R: A string representing the recipients of the transfers.
    V: An array of integers representing the values of the transfers.

  Returns:
    An array of two integers representing the minimum initial account balances for banks A and B.
  """
  
  # Initialize the initial balances for both banks.
  initialBalanceA = 0
  initialBalanceB = 0
  # Initialize the current balances for both banks.
  currentBalanceA = 0
  currentBalanceB = 0

  # Iterate over the transfers.
  for i in range(len(R)):
    # Check if the current transfer is sent to bank A.
    if R[i] == "A":
      # Update the current balance for bank A.
      currentBalanceA += V[i]
      # Update the current balance for bank B.
      currentBalanceB -= V[i]
      # Update the minimum initial balance for bank B.
      initialBalanceB = min(initialBalanceB, currentBalanceB)
    else:
      # Update the current balance for bank B.
      currentBalanceB += V[i]
       # Update the current balance for bank A.
      currentBalanceA -= V[i]
       # Update the minimum initial balance for bank A.
      initialBalanceA = min(initialBalanceA, currentBalanceA)
  # Return the minimum initial balances for both banks.
  return [abs(initialBalanceA), abs(initialBalanceB)]
    
print(solution("BAABA", [2, 4, 1, 1, 2]))  # Output: [2, 4]
print(solution("ABAB", [10, 5, 10, 15]))  # Output: [0, 15]
print(solution("B", [100]))  # Output: [100, 0]