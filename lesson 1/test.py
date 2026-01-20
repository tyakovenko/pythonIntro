#TODO: write a for loop (nest) to calculate the dot product of two matrices
#TODO: Bonus: get user input for the matrices and do the same dot product operation
#TODO: Bonus: format it all nicely
'''
Hints: 
1). Look up how to claculate the dot product and write it out exactly on paper for your matrics
2). Include a check on whether a dot product CAN be calculated within 2 matrics -> check dimensions and if the dimensions do not match up correctly print it out and break the program
'''


#example of how to calculate the dot product
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sample 3x2 matrix B
matrix_b = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Initialize the result matrix with zeros
# Result dimensions will be (rows of A) x (cols of B)
result = [[0, 0], [0, 0], [0, 0]]

# 1. Iterate through rows of matrix_a
for i in range(len(matrix_a)):
    # 2. Iterate through columns of matrix_b
    for j in range(len(matrix_b[0])):
        # 3. Iterate through rows of matrix_b (the common dimension)
        for k in range(len(matrix_b)):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

# Output the result
for row in result:
    print(row)