def solution(A, B):
  """Finds the largest possible square that can be made from two sticks of lengths A and B.

  Args:
    A: The length of the first stick.
    B: The length of the second stick.

  Returns:
    The length of the largest possible square, or 0 if no square can be made.
  """

  # Find the minimum and maximum of A and B.
  minAB = min(A, B)
  maxAB = max(A, B)

  # Find the ideal side length of the largest possible square.
  idealSide = (A + B) // 4

  # If the ideal side length is less than 1, then it is not possible to make any square.
  if idealSide < 1:
    return 0
  else:
    # If the minimum stick length is less than the ideal side length, then the
    # largest possible square will have a side length equal to the maximum stick
    # length divided by 4.
    if minAB < idealSide:
      return max(maxAB // 4, minAB)
    else:
      # If the minimum stick length divided by the ideal side length is less
      # than 2, and the maximum stick length divided by the ideal side length
      # is greater than 2, then the largest possible square will have a side
      # length equal to the ideal side length.
      if minAB // idealSide < 2 and maxAB // idealSide > 2:
        return idealSide
      else:
        # Otherwise, the largest possible square will have a side length equal
        # to the minimum of the maximum stick length divided by 2 and the
        # minimum stick length divided by 2.
        return min(maxAB // 2, minAB // 2)

  return idealSide

print(solution(10, 21))  # Output: 7
print(solution(13, 11))  # Output: 5
print(solution(2, 1))  # Output: 0
print(solution(1, 8))  # Output: 2