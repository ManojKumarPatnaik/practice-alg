def solution(S):
  """
  Given a string S of length N consisting only of letters 'A' and/or 'B', returns the minimum number of letters that need to be deleted from S in order to obtain a string in the format "A...AB...B" (all letters 'A' occur before all letters 'B').

  Args:
    S: A string of length N consisting only of letters 'A' and/or 'B'.

  Returns:
    The minimum number of letters that need to be deleted from S in order to obtain a string in the format "A...AB...B".
  """  

  # Initialize counters for 'A' and 'B'
  countA = S.count('A')
  countB = 0

  # Initialize the minimum deletions with the count of 'A'
  # This corresponds to the case where we delete all 'A's
  minDeletions = countA

  for char in S:
    if char == "A":
      # If we encounter an 'A', we decrease the count of 'A'.
      # 'A' at the right position so no need to be deleted.
      countA -= 1
    else:
      # If we encounter a 'B', we increase the count of 'B'
      # 'B' at the wrong position so need to be deleted
      countB += 1

    # The number of deletions is the sum of current counts of 'A' and 'B',
    # This is number of deletions at the current position to make the correct format
    deletions = countA + countB

    # Update the minimum deletions
    minDeletions = min(minDeletions, deletions)

  return minDeletions

print(solution('BAAABAB'))  # Output: 2
print(solution('BBABAA'))  # Output: 3
print(solution('AABBBB'))  # Output: 0
