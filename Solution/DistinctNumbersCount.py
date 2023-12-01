def solution(A):
  """
  Returns the minimum number of integers that must be deleted from A
  so that every remaining value occurs a unique number of times.

  Args:
    A: A list of integers.

  Returns:
    The minimum number of integers that must be deleted from A.
  """

  # Create a dictionary to store the frequency of each element in the array.
  freqNumbers = {}
  for number in A:
    if number not in freqNumbers:
      freqNumbers[number] = 0
      freqNumbers[number] += 1

  # Get the frequencies of all elements in the array, sorted in descending order.
  freq = sorted([count for count in freqNumbers.values()], reverse=True)

  # Initialize the number of deletions.
  deletion = 0

  # Iterate over the frequencies, starting from the second element.
  # For each frequency, check if it is greater than or equal to the previous frequency.
  # If it is, then decrement the frequency and increment the number of deletions.
  for i in range(1, len(freq)):
    while freq[i] >= freq[i - 1] and freq[i] > 0:
      freq[i] -= 1
      deletion += 1

  # Return the number of deletions.
  return deletion

print(solution([1, 1, 1, 2, 2, 2]))  # Output: 1
print(solution([5, 3, 3, 2, 5, 2, 3, 2]))  # Output: 2
print(solution([127, 15, 3, 8, 10]))  # Output: 4
print(solution([10000000, 10000000, 5, 5, 5, 2, 2, 2, 0, 0]))  # Output: 4