def solution(D, C, P):
  """
  Finds the maximum total number of orders that can be fulfilled.

  Args:
    D: A list of integers representing the distances of the orders from the store.
    C: A list of integers representing the number of monitors required for each order.
    P: The total number of monitors available.

  Returns:
    The maximum total number of orders that can be fulfilled.
  """

  # Sort the orders by increasing distance from the store.
  orders = sorted(zip(D, C), key=lambda x: (x[0], x[1]))

  # Iterate over the sorted orders.
  maxOrders = 0
  totalQuantities = 0
  for distance, quantity in orders:
    totalQuantities += quantity
    # If the current order requires more monitors than available, stop it.
    if totalQuantities > P:
      break
    maxOrders += 1

  # Return the maximum number of orders fulfilled.
  return maxOrders

print(solution([5, 11, 1, 3],[6, 1, 3, 2],7))  # Output: 2
print(solution([10, 15, 1],[10, 1, 2],3))  # Output: 1
print(solution([11, 18, 1],[9, 18, 8],7))  # Output: 0
print(solution([1, 4, 2, 5],[4, 9, 2, 3],19))  # Output: 4
