def local_maximums(grid):


    result = []

    for i in range(len(grid)-2):
        row_result = []

        for j in range(len(grid)-2):
            biggest = 0 # could change to biggest = grid[i][j], just in case grid has negative numbers

            for r in range(i, i+3):
                for c in range(j, j+3):
                    if grid[r][c] > biggest:
                        biggest = grid[r][c]

            row_result.append(biggest)

        result.append(row_result)
    return result


grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))


'''
We are given a n x n matrix
we need to return a matrix of n-2 x n-2

each number in the matrix comes from the largest number from the respective 3x3


'''