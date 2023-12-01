def solution(N):
  """Returns the smallest non-negative integer whose individual digits sum to N.

  Args:
    N: An integer within the range [0..50].

  Returns:
    An integer whose individual digits sum to N.
  """

  # Initialize the result and the number of 9s that were subtracted from the original number.
  digits = []

  # Repeatedly subtract 9 from N until it is less than 9.
  while N > 9:
    digits.append("9")
    N -= 9

  digits.append(str(N))
  # Reverse the result and return it.
  return int("".join(reversed(digits)))
    
print(solution(16))  # Output: 79
print(solution(19))  # Output: 199
print(solution(7))  # Output: 7