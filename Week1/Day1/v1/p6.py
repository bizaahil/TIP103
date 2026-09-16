def harvest(vegetable_patch):

    result = 0
    n = len(vegetable_patch)
    m = len(vegetable_patch[0])

    for i in range(n):
        for j in range(len(vegetable_patch[i])):
            if vegetable_patch[i][j] == 'c':
                result += 1
    return result

vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch))


'''
We are given an n x m matrix
n = len(vegetable_patch)
m = len(vegetable_patch[0])

we return # of carrots ready to harvest (c)

Implement:

Enhanced for loop, traverse through n and inside traverse m with [n][m]
Anytime we see vegtable_patch[n][m] == 'c', result += 1



'''