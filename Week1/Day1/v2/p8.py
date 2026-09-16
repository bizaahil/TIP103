def defuse(code, k):

    new_array = []
    sum = 0
    n = len(code)

    if k == 0:
        for i in range(len(code)):
            new_array.append(0)
        return new_array


    for i in range(n):
        total = 0

        if k > 0:
            for step in range(1, k + 1):
                index = (i + step) % n
                total += code[index]

        else:
            for step in range(1, abs(k) + 1):
                index = (i - step) % n
                total += code[index]

        new_array.append(total)

    return new_array

code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))



'''

so we have an array of numbers
we are given an int k

we want to return an array of ints that are modified based on if k > 0, k < 0, or k = 0

my plan
we make a new array
we traverse thru original array and depending on index we add sum of k elements (eitehr forward or backward)
we take sum and store it in new array based on the index we were dealing with, and when we're done we return new array


'''
