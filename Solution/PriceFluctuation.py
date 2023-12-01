def solution(A):
  """
  Calculates the maximum income that could be made from a historical record of asset prices.

  Args:
    A (list[int]): An array of historical asset prices.

  Returns:
    int: The maximum income achievable, modulo 1,000,000,000.
  """

  totalSell = 0  # Initialize the total selling income
  totalBuy = 0  # Initialize the total buying cost
  isHolding = True  # Initialize a flag indicating whether we are currently holding an asset

  for i in range(len(A) - 1):  # Iterate through the array of prices
    if isHolding:  # If we are currently holding an asset
      if A[i] > A[i + 1]:  # If the current price is higher than the next price
        totalSell += A[i]  # Sell the asset at the current price
        isHolding = False  # Update the flag to indicate we are not holding an asset
      else:  # If the current price is lower than or equal to the next price
        continue  # Hold the asset and wait for a better selling opportunity
    else:  # If we are not currently holding an asset
      if A[i] < A[i + 1]:  # If the current price is lower than the next price
        totalBuy += A[i]  # Buy the asset at the current price
        isHolding = True  # Update the flag to indicate we are holding an asset
      else:  # If the current price is higher than or equal to the next price
        continue  # Don't buy the asset, wait for a better buying opportunity

  if isHolding:  # If we are still holding an asset at the end of the array
    totalSell += A[-1]  # Sell the asset at the last price

  return (totalSell - totalBuy) % 1000000000  # Calculate the maximum income and return it modulo 1,000,000,000

print(solution([4, 1, 2, 3]))  # Output: 6
print(solution([1, 2, 3, 3, 2, 1, 5]))  # Output: 7
print(solution([1000000000, 1, 2, 2, 1000000000, 1, 1000000000]))  # Output: 999999998
