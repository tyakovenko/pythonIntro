import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #array data type; makes numpy operations easier when working with this array than classic
arrReg = [1, 'hi', 2]
#most of the time you would walk to have np arrays
#significantly faster and more memory efficient
#MUST have object of the same data type

#ex: dot product of two matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_b = [
    [1, 2],
    [3, 4],
    [5, 6]
]
result = np.dot(matrix_a, matrix_b) #we can also use an @ function to do the same np.array(matrix_a) @ np.array(matrix_b)
print(result)
print(np.array(matrix_a) @ np.array(matrix_b))

#simple data manipulation can be done with these using element wise operations
quantities = np.array([10, 5, 20, 1])
prices = np.array([1.50, 12.00, 0.75, 50.00])
subtotals = quantities * prices #in standard python arrays, we would need a loop to do this multiplication
total_revenue = np.sum(subtotals) #various aggrigate functions readily available
print(f"Subtotals: {subtotals}")
print(f"Total Revenue: ${total_revenue}")

#key Features
#mapping/broadcasting
discounted_prices = prices * 0.90
print(discounted_prices)
#indexing and slicing
first_two = prices[:2]
print(first_two)
#filtering
expensive_items = prices[prices > 10]
print(expensive_items)

arr = np.array([5, 1, 2, 1, 5, 3])

# Get unique values and the index of their first appearance
_, idx = np.unique(arr, return_index=True)

# Sort the indices to maintain original order
unique_ordered = arr[np.sort(idx)]
print(unique_ordered)

