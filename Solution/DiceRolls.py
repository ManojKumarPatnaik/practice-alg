def solution(A, F, M):
  """
  Finds the possible results of the missing dice rolls.

  Args:
    A: A list of the remembered dice roll results.
    F: The number of missing dice roll results.
    M: The arithmetic mean of all the dice roll results.

  Returns:
    A list of the possible results of the missing dice rolls, or [0] if no
    such results exist.
  """

  # Calculate the total number of dice rolls.
  N = len(A) + F

  # Calculate the sum of the remembered dice roll results.
  totalB = (N * M) - sum(A)

  # Calculate the estimated value of the missing dice rolls without rounding.
  estRoll = totalB / F

  # If the estimated value is under 1 or over 6, there are no possible results.
  if estRoll < 1 or estRoll > 6:
    return [0]

  # Missing rolls are rounded values of the estimated value
  B = [int(estRoll)] * F

  # If there are the remaining value, increase missing rolls one by one.
  remaining = totalB % F
  if remaining > 0:
    for i in range(F):
      B[i] += 1
      remaining -= 1
      if remaining < 1:
        break

  # Return the list of possible results of the missing dice rolls.
  return B

print(solution([3, 2, 4, 3], 2, 4))  # Output: [6, 6]
print(solution([1, 5, 6], 4, 3))  # Output: [3, 2, 2, 2]
print(solution([1, 2, 3, 4], 4, 6))  # Output: [0]
print(solution([6, 1], 1, 1))  # Output: [0]
