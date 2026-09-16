def diagonal_sum(grid):

    sum = 0

    # add first diagonal
    for i in range(len(grid)):
        sum += grid[i][i] #this gets (0,0)(1,1)(2,2)...

    # add second diagonal
    x = 0
    y = len(grid) -1

    while(y >= 0):
        sum += grid[x][y]
        x+=1
        y-=1

    #delete common num for odd matricies

    if len(grid) % 2 != 0:
        z = len(grid) // 2
        sum -= grid[z][z]

    return sum




grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(grid))

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(diagonal_sum(grid))

grid = [
	[5]
]
print(diagonal_sum(grid))
'''

We are given an n x n matrix 
we have to return the sums of the diagonals, but not double count (only happens with odd integers greater than or equal to 3)

my plan 
for first diagonal we add (0,0) (1,1) (2,2) (3,3)..stop at n-1
for second diagonal we add (0, 3)(1, 2), (2, 1), (3,0)  we can see no int goes to n but to n-1

so first diagonal we add 1 to each pair
for 2nd we add 1 to first num, and subract for second num

at the end if the len(grid) is >=3 and % 2 != 0
then we take the len(grid) // 2 and then subtract that pair from sum
then return sum


'''