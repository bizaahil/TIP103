def non_decreasing(nums):


    fail = 0

    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            pass
        else:
            fail += 1

    if fail > 1:
        return False
    return True


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))