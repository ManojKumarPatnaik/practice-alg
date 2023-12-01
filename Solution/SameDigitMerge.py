def solution(numbers):
  """
  Counts the number of pairs of numbers in the given array with the same first and last digits.

  Args:
    numbers: A list of integers, each with at least two digits and different first and last digits.

  Returns:
    The number of pairs of numbers in the given array with the same first and last digits.
  """

  # Create a dictionary where the keys are the first and last digits of the numbers,
  # and the values are the counts of the numbers with those digits.
  digitCounts = {}
  for number in numbers:
    firstDigit = int(str(number)[0])
    lastDigit = int(str(number)[-1])
    digitCounts[(firstDigit, lastDigit)] = digitCounts.get((firstDigit, lastDigit), 0) + 1

  # Calculate the number of pairs.
  pairs = 0
  for (firstDigit, _), firstCount in digitCounts.items():
    for (_, lastDigit), lastCount in digitCounts.items():
      if firstDigit == lastDigit:
        pairs += firstCount * lastCount

  return pairs

print(solution([30, 12, 29, 91]))  # Output: 3
print(solution([122, 21, 21, 23]))  # Output: 5
