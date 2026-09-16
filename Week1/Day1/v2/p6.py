def smaller_than_current(nums):

    count = 0
    arr = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i] and nums[j] != nums[i]:
                count+=1

        arr.append(count)
        count = 0

    return arr



nums = [8, 1, 2, 2, 3]
print(smaller_than_current(nums))

nums = [6, 5, 4, 8]
print(smaller_than_current(nums))

nums = [7, 7, 7, 7]
print(smaller_than_current(nums))