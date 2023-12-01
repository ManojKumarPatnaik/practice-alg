def solution(N):
  """Returns the smallest integer greater than N that does not contain two identical consecutive digits.

  Args:
    N: A positive integer.

  Returns:
    The smallest integer greater than N that does not contain two identical consecutive digits.
  """

  # Initialize the variable `noEqualDigits` to N + 1.
  noEqualDigits = N + 1

  # While `noEqualDigits` is greater than N, iterate.
  while noEqualDigits > N:

    # Check if all the digits in `noEqualDigits` are different.
    if all([str(noEqualDigits)[i] != str(noEqualDigits)[i + 1] for i in range(len(str(noEqualDigits)) - 1)]):

      # If all the digits are different, break the loop.
      break

    # Otherwise, increment `noEqualDigits` by 1.
    noEqualDigits += 1

  # Return `noEqualDigits`.
  return noEqualDigits

print(solution(55))  # Output: 56
print(solution(1765))  # Output: 1767
print(solution(98))  # Output: 101
print(solution(44432))  # Output: 45010
print(solution(3298))  # Output: 3401
