def solution(S):
  # Convert the string to a list of integers
  digits = [int(d) for d in S]
  # Calculate the initial sum of the digits
  total = sum(digits)
  # Initialize the count of numbers divisible by 3
  count = 0

  # Check if the number itself is divisible by 3.
  if total % 3 == 0:
    count += 1

  # Iterate over each digit
  for digit in digits:
    # Calculate the remaining sum after removing the current digit
    remaining = total - digit
    # Check all possible replacements for the current digit
    for replacement in range(10):
    # If the new sum is divisible by 3, increment the count
      if (remaining + replacement) % 3 == 0 and replacement != digit:
        count += 1
  # Return the count of numbers divisible by 3
  return count

print(solution("23"))  # Output: 7
print(solution("0081"))  # Output: 11
print(solution("022"))  # Output: 9
