def solution(A, K):
  """Prints a string representing the formatted array A.

  Args:
    A: A non-empty array of N integers.
    K: The number of numbers in each row of the table.
  """

  # Create a list of lists to store the table.
  table = []

  # Iterate over the array A and add each number to the first empty row in the table.
  # If all rows in the table are full, create a new empty row and add the number to that row.
  for i in range(0, len(A), K):
    table.append(A[i:i + K])

  # Find the maximum number of digits in any number in the table.
  maxDigits = len(str(max(A)))

  # Print the table header.
  print("+" + ("-" * maxDigits + "+") * len(table[0]))

  # Iterate over the table and print each row.
  for row in table:
    # Print the row separator.
    print("|", end="")

    # Iterate over the numbers in the row and print each number.
    for number in row:
      # Calculate the number of spaces needed to pad the number to the maximum number of digits.
      digits = len(str(number))
      padding = " " * (maxDigits - digits)

      # Print the number with the appropriate padding.
      print(padding + str(number) + "|", end="")

    # Print the row separator.
    print("\n" + "+" + ("-" * maxDigits + "+") * len(row) + "\n", end="")
    
solution([4, 35, 80, 123, 12345, 44, 8, 5], 10)
solution([4, 35, 80, 123, 12345, 44, 8, 5, 24, 3], 4)
solution([4, 35, 80, 123, 12345, 44, 8, 5, 24, 3, 22, 35], 4)
