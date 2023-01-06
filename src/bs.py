import math


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = math.floor((left + right) / 2)

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


print(search([-1,0,3,5,9], 9))
