def wealthiest_customer(accounts):

    index = 0
    sum = 0
    largest = 0
    arr = []


    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            sum += accounts[i][j]

        if sum > largest:
            largest = sum
            index = i
            arr = [index, sum]
            
        sum = 0

    return arr

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts))




'''

we are given a 2d int array
we have to return an array with 2 ints: first int is which array has the highest output and 2nd int is what is that output


my plan:
traverse through every sub array and if the sum is largest then we save that sum along with the index of it
we return at the end which index and sum was largest 


'''