def find_missing_clues(clues, lower, upper):

    arr = []

    start = None

    for num in range(lower, upper+1):
        # the start
        if num not in clues:
            if start is None:
                start = num


        # the end
        else:
            if start is not None:
                end = num-1
                arr.append([start, end])
                start = None

    if start is not None:
        arr.append([start, upper])

    return arr

            
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
            







'''
we are given an array of ints
we are given a lowe and upper bound

we have to find ranges that cover all the missing numbers in ranges

plan

iterate from lower to upper
every time that num isnt in clues we add that range starting and if we reach a num thats in clues we add the num-1 as the end 

'''