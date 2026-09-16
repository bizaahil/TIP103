def non_decreasing(nums):
    

    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            return True

    return False


'''
#create variable false

if number to the right is ever bigger than the left, then change to true




'''


nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))